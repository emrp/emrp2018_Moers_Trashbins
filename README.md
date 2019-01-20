# emrp2018_Moers_Trashbins
This tutorial shows you how to measure the trash level of trashbins using the VL53L0X time-of-flight sensor, Heltec WIFI LoRA 32 (V2) board, The Things Network (TTN) and ... database.
## 1. Hardware Requirements
The following pieces of hardware are required for this tutorial:
- VL53L0X break-out board. You can get one here from Adafruit: https://www.adafruit.com/product/3317
- WIFI LoRA 32 (V2) board with antenna. This board includes an ESP32 microcontroller, an SX125x LoRa module. For more information: http://www.heltec.cn/project/wifi-lora-32/?lang=en

## 2. Software installation
### 2.1 Arduino IDE
Download and install the Arduino IDE from: https://www.arduino.cc/en/main/software

### 2.2 Libraries
Heltec support two sets of libraries to simplify the use of the integrated OLED, LoRa and other modules of the WIFI LoRA 32 (V2) board.

#### 2.2.1 Heltec board support package
Download the repository [WiFi_Kit_series] (https://github.com/Heltec-Aaron-Lee/WiFi_Kit_series) as zip and extract it to `/Documents/Arduino/hardware/heltec`. Create the folders manually if they have not been created.

Navigate to `/Documents/Arduino/hardware/heltec/esp32/tools`, double-click on `get.exe` and wait for the script to finish.

Make sure the following folders are generated:

#### 2.2.2 Heltec extended libraries
Download the repository [Heltec_ESP32] (https://github.com/HelTecAutomation/Heltec_ESP32) as zip and extract it to /Documents/Arduino/.

Plug in the heltec board and wait for the drivers to install (if needed).

Open the Arduino IDE, click on `Tools->Boards` and choose `Wifi_LoRa_32_V2`.

Click on `Sketch->Include Library->Add .Zip Libaries...`.

In the pop-up window, navigate to `/Documents/Arduino/` and choose `Heltec_ESP32-master.zip`.

#### 2.2.3 Running an example
Make sure the chosen board is `Wifi_LoRa_32_V2`.

Click on \
`File->Examples->(Example from Custom Libraries)->Heltec ESP32 Dev-Boards->OLED->SSD1306SimpleDemo`.

Click the Upload button to upload the program to the board.


