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

#include <Wire.h>
#include "MAX30101.h"

MAX30101 ppg;

#define debug Serial //Uncomment this line if you're using an Uno or ESP
//#define debug SerialUSB //Uncomment this line if you're using a SAMD21

void setup()
{
  debug.begin(9600);
  debug.println("MAX30101 Basic Readings Example");

  // Initialize sensor
  if (ppg.begin() == false)
  {
    debug.println("MAX30101 was not found. Please check wiring/power. ");
    while (1);
  }

  ppg.setup(); //Configure sensor. Use 6.4mA for LED drive
}

void loop()
{
  debug.print(" R[");
  debug.print(ppg.getRed());
  debug.print("] IR[");
  debug.print(ppg.getIR());
  debug.print("] G[");
  debug.print(ppg.getGreen());
  debug.print("]");

  debug.println();
}
