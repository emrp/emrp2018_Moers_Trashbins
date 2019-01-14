#include <HardwareSerial.h>
#include <lmic.h>
#include <hal/hal.h>
#include <SPI.h>
#include <DHT.h>
#include <DHT_U.h>
#include "SSD1306.h" 
#include <CayenneLPP.h>
#include "Adafruit_VL53L0X.h"

#define BUILTIN_LED 25
#define L0X_SHUTDOWN 17

SSD1306    display(0x3c, 4, 15, 16); //SDA = 4, SCL = 15, RST = 16
Adafruit_VL53L0X lox; // time-of-flight infarred sensor
CayenneLPP lpp(51);

static int16_t Distance = 0;

// This EUI must be in little-endian format, so least-significant-byte
// first. When copying an EUI from ttnctl output, this means to reverse
// the bytes. For TTN issued EUIs the last bytes should be 0xD5, 0xB3, 0x70.
static const u1_t PROGMEM APPEUI[8] = { 0xCC, 0x46, 0x01, 0xD0, 0x7E, 0xD5, 0xB3, 0x70 };
void os_getArtEui (u1_t* buf) {
  memcpy_P(buf, APPEUI, 8);
}
// This should also be in little endian format, see above.
static const u1_t PROGMEM DEVEUI[8] = { 0x41, 0x64, 0x0E, 0x6E, 0xC4, 0x2F, 0x61, 0x00 };
void os_getDevEui (u1_t* buf) {
  memcpy_P(buf, DEVEUI, 8);
}
// This key should be in big endian format (or, since it is not really a
// number but a block of memory, endianness does not really apply). In
// practice, a key taken from ttnctl can be copied as-is.
// 
static const u1_t PROGMEM APPKEY[16] = { 0x15, 0x29, 0x64, 0x26, 0x64, 0x82, 0x64, 0xD1, 0x1A, 0xF7, 0x82, 0xDC, 0x60, 0xB8, 0xE1, 0x36 };
void os_getDevKey (u1_t* buf) {
  memcpy_P(buf, APPKEY, 16);
}
static osjob_t sendjob;
// Schedule TX every this many seconds (might become longer due to duty
// cycle limitations).
const unsigned TX_INTERVAL = 10;
// Pin mapping
const lmic_pinmap lmic_pins = {
  .nss = 18,
  .rxtx = LMIC_UNUSED_PIN,
  .rst = 14,
  .dio = {26, 33, 32},
};

void onEvent (ev_t ev) {
  display.clear();
  switch (ev) {
    case EV_SCAN_TIMEOUT:
      Serial.println(F("EV_SCAN_TIMEOUT"));
      display.drawString(0, 7, "EV_SCAN_TIMEOUT");
      break;
    case EV_BEACON_FOUND:
      Serial.println(F("EV_BEACON_FOUND"));
      display.drawString(0, 7, "EV_BEACON_FOUND");
      break;
    case EV_BEACON_MISSED:
      Serial.println(F("EV_BEACON_MISSED"));
      display.drawString(0, 7, "EV_BEACON_MISSED");
      break;
    case EV_BEACON_TRACKED:
      Serial.println(F("EV_BEACON_TRACKED"));
      display.drawString(0, 7, "EV_BEACON_TRACKED");
      break;
    case EV_JOINING:
      Serial.println(F("EV_JOINING"));
      display.drawString(0, 7, "EV_JOINING   ");
      break;
    case EV_JOINED:
      Serial.println(F("EV_JOINED"));
      display.drawString(0, 7, "EV_JOINED    ");
      // Disable link check validation (automatically enabled
      // during join, but not supported by TTN at this time).
      LMIC_setLinkCheckMode(0);
      break;
    case EV_RFU1:
      Serial.println(F("EV_RFU1"));
      display.drawString(0, 7, "EV_RFUI");
      break;
    case EV_JOIN_FAILED:
      Serial.println(F("EV_JOIN_FAILED"));
      display.drawString(0, 7, "EV_JOIN_FAILED");
      break;
    case EV_REJOIN_FAILED:
      Serial.println(F("EV_REJOIN_FAILED"));
      display.drawString(0, 7, "EV_REJOIN_FAILED");
      //break;
      break;
    case EV_TXCOMPLETE:
      Serial.println(F("EV_TXCOMPLETE (includes waiting for RX windows)"));
      display.drawString(0, 7, "EV_TXCOMPLETE");
      digitalWrite(BUILTIN_LED, LOW);
      if (LMIC.txrxFlags & TXRX_ACK) {
        Serial.println(F("Received ack"));
        display.drawString(0, 7, "Received ACK");
      }
      if (LMIC.dataLen) {
        Serial.println(F("Received "));
        display.drawString(0, 6, "RX ");
        Serial.println(LMIC.dataLen);
        //display.setCursor(4, 6);
        display.printf("%i bytes", LMIC.dataLen);
        Serial.println(F(" bytes of payload"));
        //display.setCursor(0, 7);
        display.printf("RSSI %d SNR %.1d", LMIC.rssi, LMIC.snr);
      }
      // Schedule next transmission
      os_setTimedCallback(&sendjob, os_getTime() + sec2osticks(TX_INTERVAL), do_send);
      break;
    case EV_LOST_TSYNC:
      Serial.println(F("EV_LOST_TSYNC"));
      display.drawString(0, 7, "EV_LOST_TSYNC");
      break;
    case EV_RESET:
      Serial.println(F("EV_RESET"));
      display.drawString(0, 7, "EV_RESET");
      break;
    case EV_RXCOMPLETE:
      // data received in ping slot
      Serial.println(F("EV_RXCOMPLETE"));
      display.drawString(0, 7, "EV_RXCOMPLETE");
      break;
    case EV_LINK_DEAD:
      Serial.println(F("EV_LINK_DEAD"));
      display.drawString(0, 7, "EV_LINK_DEAD");
      break;
    case EV_LINK_ALIVE:
      Serial.println(F("EV_LINK_ALIVE"));
      display.drawString(0, 7, "EV_LINK_ALIVE");
      break;
    default:
      Serial.println(F("Unknown event"));
      //display.setCursor(0, 7);
      //display.printf("UNKNOWN EVENT %d", ev);
      break;
  }
  display.display();
}
void do_send(osjob_t* j) {
  // Check if there is not a current TX/RX job running
  if (LMIC.opmode & OP_TXRXPEND) {
    Serial.println(F("OP_TXRXPEND, not sending"));
    display.drawString(0, 7, "OP_TXRXPEND, not sent");
  } else {     
    delay(100);

    // Measure distance
    L0X_init();
    Distance = L0X_getDistance();
    L0X_deinit();

    lpp.reset();
    lpp.addDigitalOutput(1, Distance);
    
    // Prepare upstream data transmission at the next possible time.
    LMIC_setTxData2(1, lpp.getBuffer(), lpp.getSize(), 0);
    
    Serial.println(F("Packet queued"));
    display.clear();
    display.drawString(0, 7, "PACKET QUEUED");
    display.display();
    digitalWrite(BUILTIN_LED, HIGH);
  }
  // Next TX is scheduled after TX_COMPLETE event.
}
void setup() { 
  Serial.begin(115200);
  Serial.println("=============================================");

  SPI.begin(5, 19, 27);
  
  pinMode(16,OUTPUT); // reset display
  digitalWrite(16, LOW);
  delay(50);
  digitalWrite(16, HIGH);
  display.init();
  display.setFont(ArialMT_Plain_10); 
  display.drawString(0, 1, "Hello");
  display.display();
  delay(1000);  
 
  // LMIC init
  os_init();
  
  // Reset the MAC state. Session and pending data transfers will be discarded.
  LMIC_reset();
  // Start job (sending automatically starts OTAA too)
  do_send(&sendjob);
  pinMode(BUILTIN_LED, OUTPUT);
  digitalWrite(BUILTIN_LED, LOW);
  display.init();
  display.clear();
  display.drawString(0, 1, "Hi");
  display.display();

  digitalWrite(L0X_SHUTDOWN, LOW);
  pinMode(L0X_SHUTDOWN, OUTPUT);
  delay(100);
}
void loop() {
  os_runloop_once();
}

void L0X_init(void)
{
  digitalWrite(L0X_SHUTDOWN, HIGH);
  //Wire.begin(21, 22, 100000);
  delay(100);
  if (!lox.begin()) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
}

void L0X_deinit(void)
{
  digitalWrite(L0X_SHUTDOWN, LOW);
}

// return distance in cm
int16_t L0X_getDistance(void)
{
  VL53L0X_RangingMeasurementData_t measure;
  int16_t distance = 0;
  for (int i = 0; i < 10; i++)
  {
    delay(100);
    Serial.print("Reading a measurement... ");
    lox.rangingTest(&measure, false); // pass in 'true' to get debug data printout!
    
    if (measure.RangeStatus != 4) {  // phase failures have incorrect data
      distance = measure.RangeMilliMeter / 10;
      Serial.print("Distance (cm): "); Serial.println(measure.RangeMilliMeter / 10);
    } else {
      Serial.println(" out of range ");
      distance = 0;
    }
  }
  return distance;
}
