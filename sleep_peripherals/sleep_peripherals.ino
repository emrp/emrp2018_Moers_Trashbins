#include <HardwareSerial.h>
#include <lmic.h>
#include <hal/hal.h>
#include <SPI.h>
#include <DHT.h>
#include <DHT_U.h>
#include "SSD1306.h" 
#include <CayenneLPP.h>
#include "Adafruit_VL53L0X.h"
#include "driver/rtc_io.h"

#define uS_TO_S_FACTOR     1000000  /* Conversion factor for micro seconds to seconds */
#define SLEEP_TIME_IN_SEC  10       /* Time ESP32 will go to sleep (in seconds) */
#define BUILTIN_LED        25
#define L0X_SHUTDOWN       17
#define VEXT               21

RTC_DATA_ATTR uint8_t BootCount = 0;

SSD1306    display(0x3c, 4, 15, 16); //SDA = 4, SCL = 15, RST = 16
Adafruit_VL53L0X lox; // time-of-flight infarred sensor

void setup() {
  Serial.begin(115200);
  Serial.println("=============================================");
  
  if (BootCount == 0)
  {
    Serial.println("\n\nFirst Boot\n\n");
    SPI.begin(5, 19, 27); // Connect to LORA module
  
    display.init();
    display.drawString(0, 1, "Hello");
    display.display();
    delay(1000);  
    display.clear();
  
    gpio_pulldown_en(GPIO_NUM_17);  
    digitalWrite(L0X_SHUTDOWN, LOW);
    pinMode(L0X_SHUTDOWN, OUTPUT);
    delay(100);
  }
  else
  {
    Serial.println("...................................");
    SPI.begin(5, 19, 27); // Connect to LORA module

    display.init();
    display.drawString(0, 1, "Hello");
    display.display();
    delay(1000);  
    display.clear();
  }
  
  Serial.print("BootCount: "); Serial.println(BootCount);
  BootCount++;

  rtc_gpio_set_direction(GPIO_NUM_2, RTC_GPIO_MODE_OUTPUT_ONLY);
  rtc_gpio_set_level(GPIO_NUM_2, HIGH);

  esp_sleep_enable_timer_wakeup(SLEEP_TIME_IN_SEC * uS_TO_S_FACTOR);
}

void loop() {
  turnOffPeripherals();
  esp_deep_sleep_start();
}

void turnOffPeripherals(void)
{
  rtc_gpio_set_level(GPIO_NUM_2, LOW);
  rtc_gpio_hold_en(GPIO_NUM_2);
}
