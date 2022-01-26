#include <ArduinoBLE.h>
#include <Arduino_LSM6DS3.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_MLX90614.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
#define I2C_MLX 0x5A // might just default to this, will have to test
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)

#define DEBUG true

// apparently it is actually supposed to be 0x3C, if does not work change to 0x3D

BLEService nanoService("a687fc14-f079-4042-bae7-fbec864bfbfb"); // BLE Service

// BLE Characteristics - custom 128-bit UUID for each package of data being sent
BLEDoubleCharacteristic accelerometerXData("fba5da1c-dc0b-4100-abf7-ab2b2b23ba08", BLERead);
BLEDoubleCharacteristic accelerometerYData("80bf7d48-23ce-4f68-93b1-4c34b81d9757", BLERead);
BLEDoubleCharacteristic accelerometerZData("04545938-d3b6-4fb5-8141-fc1f5849ffa5", BLERead);
BLEDoubleCharacteristic temperatureData("a7361e96-1414-4926-a415-91e5cabfe126", BLERead);
BLEDoubleCharacteristic ppgData("13e9f3cc-0caf-472f-963b-5458cca2d734", BLERead);

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
    Serial.begin(9600);
    
    if (DEBUG) {
      while(!Serial);
    }

    if (!IMU.begin()) {
      Serial.println("Failed to initialize IMU!");
      while(1);
    }

    else Serial.println("IMU initialization successful");

    Serial.print("Accelerometer sample rate = ");
    Serial.print(IMU.accelerationSampleRate());
    Serial.println(" Hz");
    Serial.println();
    Serial.println("Acceleration in G's");
    Serial.println("X\tY\tZ");

    if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
      Serial.println("SSD1306 allocation failed");
      while(1);
    }

    else Serial.println("OLED connection successful");

    if (!mlx.begin(I2C_MLX)) {
      Serial.println("Error connecting to MLX sensor. Check wiring.");
      while (1);
    }

    else Serial.println("MLX sensor connection successful");
    
    if (!BLE.begin()) {
        Serial.println("Starting BLE failed!");
        while (1);
    }

    else Serial.println("BLE initialization successful");
  
    // set advertised local name and service UUID:
    BLE.setLocalName("Your Health Sensor");
    BLE.setAdvertisedService(nanoService);

    // add the characteristic to the service
    nanoService.addCharacteristic(accelerometerXData);
    nanoService.addCharacteristic(accelerometerYData);
    nanoService.addCharacteristic(accelerometerZData);

    // add service
    BLE.addService(nanoService);

    // set the initial value for the characeristic:
    accelerometerXData.writeValue(0.0);
    accelerometerYData.writeValue(0.0);
    accelerometerZData.writeValue(0.0);
    ppgData.writeValue(0.0);
    temperatureData.writeValue(0.0);

    // start advertising
    BLE.advertise();
    delay(100);
    Serial.println("Open to connection");
}

void loop() {
    float x, y, z;
    // listen for BLE centrals to connect:
    BLEDevice central = BLE.central();

    // if a central is connected to peripheral:
    if (central) {
        Serial.print("Connected to peripheral: ");
        // print the central's MAC address:
        Serial.println(central.address());

        // while the central is still connected to peripheral:
        while (central.connected()) {
            if (IMU.accelerationAvailable()) {
              IMU.readAcceleration(x, y, z);
  
              Serial.print(x);
              Serial.print('\t');
              Serial.print(y);
              Serial.print('\t');
              Serial.println(z);
              
              accelerometerXData.writeValue(x);
              accelerometerYData.writeValue(y);
              accelerometerZData.writeValue(z);
            }
        }

        // when the central disconnects, print it out:
        Serial.print(F("Disconnected from central: "));
        Serial.println(central.address());
    }
}
