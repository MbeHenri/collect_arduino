// REQUIRES the following Arduino libraries:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

// DHT Sensor Library (à installer)
#include "DHT.h"
#define DHTTYPE DHT11 // DHT11
#define PIN_TEMP_HUMIDITY 2

DHT dht_ = DHT(PIN_TEMP_HUMIDITY, DHTTYPE);

float t;
float h;
void setup() {
  Serial.begin(9600);
  dht_.begin();
}

void loop() {
  t = dht_.readTemperature();
  h = dht_.readHumidity();
  delay(1000);
  Serial.print(t);
  Serial.print(';');
  Serial.println(h);
}

