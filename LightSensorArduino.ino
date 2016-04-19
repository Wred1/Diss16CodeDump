#include <Wire.h>                  // Imports library for i^2C
#include <BH1750.h>                // Imports library for light sensor
#include <LiquidCrystal.h>         // Imports library for screen control

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // Sets pinout for screen


BH1750 lightMeter;                 // Starts light sensor process


void setup(){                      // -- SETUP--
  lcd.begin(8, 2);                 // Starts screen, sets as a 8x2 screen
  lightMeter.begin();              // Starts light meter communication

  lcd.setCursor(0, 0);             // Sets cursor to top left
  lcd.print("Booting");            // Writes 'booting'

  delay(3000);                     // Delays for 3s for initialisation
  lcd.clear();                     // Clears screen ready for measurements
}


void loop() {                      // -- MAIN LOOP --
  uint16_t lux = lightMeter.readLightLevel(); // Takes light measurement

  lcd.clear();                     // Clears LCD from previous measurement
  lcd.setCursor(0, 0);             // Sets cursor top left
  lcd.print("Light=");             // Prints 'Light=' onscreen
  lcd.setCursor(0, 1);             // Sets cursor to bottom row
  lcd.print(lux);                  // Prints measured lux value
  lcd.print("Lx");                 // Prints word 'lx'   
  delay(1000);                     // Delays for 1s (time between measurements)
}                                  // End of loop
