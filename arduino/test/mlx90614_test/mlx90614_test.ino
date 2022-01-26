/***************************************************
  This is a library example for the MLX90614 Temp Sensor

  Designed specifically to work with the MLX90614 sensors in the
  adafruit shop
  ----> https://www.adafruit.com/products/1747 3V version
  ----> https://www.adafruit.com/products/1748 5V version

  These sensors use I2C to communicate, 2 pins are required to
  interface
  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing
  products from Adafruit!

  Written by Limor Fried/Ladyada for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ****************************************************/
//#include <Wire.h>
//
//void setup() {
//  Serial.begin(9600);
//  while(!Serial);
//  Wire.beginTransmission(0x5A);
//  Wire.write(0x07); // read ram address 7(Temp object 1)
//  Wire.endTransmission(false);
//  //The SMBus communication will only respond with 3 bytes: data low, data high, and PEC (is CRC-8)
//}
//
//void loop() {
//  Wire.requestFrom(0x5A, 3,true); // request 3 bytes from slave device
//  unsigned int r = Wire.read(); // receive a byte as character
//  r |= (Wire.read()<<8);
//  Serial.println(r);
//}

//float k = r*0.02; //temp in kelvin
//float c = k-273.15;
//float f = (9*c/5)+32; //fahrenheit
//Serial.print(f); // print the character
//Serial.print(' ');
//c = Wire.read();
//Serial.println();

#include <Adafruit_MLX90614.h>
#define I2C_MLX 0x5A // might just default to this, will have to test

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

void setup() {
  Serial.begin(11520);
  while (!Serial);

  Serial.println("MLX90614 test");
  if (!mlx.begin(I2C_MLX)) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };
//  mlx.begin();
  Serial.print("Emissivity = "); Serial.println(mlx.readEmissivity());
  Serial.println("================================================");
}

void loop() {
  Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempC());
  Serial.print("*C\tObject = "); Serial.print(mlx.readObjectTempC()); Serial.println("*C");
  Serial.print("Ambient = "); Serial.print(mlx.readAmbientTempF());
  Serial.print("*F\tObject = "); Serial.print(mlx.readObjectTempF()); Serial.println("*F");

  Serial.println();
  delay(500);
}
