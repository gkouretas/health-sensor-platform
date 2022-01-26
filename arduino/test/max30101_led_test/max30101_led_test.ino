/*
  MAX30105 Breakout: Output all the raw Red/IR/Green readings
  By: Nathan Seidle @ SparkFun Electronics
  Date: October 2nd, 2016
  https://github.com/sparkfun/MAX30105_Breakout

  Outputs all Red/IR/Green values.

  Hardware Connections (Breakoutboard to Arduino):
  -5V = 5V (3.3V is allowed)
  -GND = GND
  -SDA = A4 (or SDA)
  -SCL = A5 (or SCL)
  -INT = Not connected

  The MAX30105 Breakout can handle 5V or 3.3V I2C logic. We recommend powering the board with 5V
  but it will also run at 3.3V.

  This code is released under the [MIT License](http://opensource.org/licenses/MIT).
*/

//#include <Wire.h>
#include "MAX30105.h"
//#include "MAX30101.h"

MAX30105 ppg;
//MAX30101 ppg;

//#define debug Serial //Uncomment this line if you're using an Uno or ESP
//#define debug SerialUSB //Uncomment this line if you're using a SAMD21

void setup()
{
  Serial.begin(9600);
  while(!Serial);
  Serial.println("MAX30101 Basic Readings Example");
//
  // Initialize sensor
//  if (ppg.begin() == false)
//  {
//    Serial.println("MAX30101 was not found. Please check wiring/power. ");
//    while (1);
//  }

  ppg.setup(); //Configure sensor. Use 6.4mA for LED drive
}

void loop() {
  Serial.println("MAX30101 Basic Readings Example");
  Serial.print(" R[");
  Serial.print(ppg.getRed());
  Serial.print("] IR[");
  Serial.print(ppg.getIR());
//  Serial.print("] G[");
//  Serial.print(ppg.getGreen());
  Serial.print("]");

  Serial.println();
}
