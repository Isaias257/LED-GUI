#include <FastLED.h>
#define NUM_LEDS  60
#define LED_PIN   2
CRGB leds[NUM_LEDS];

String readString;

int pin = 10;
int R_index, red;
int G_index, green;
int B_index, blue;
String Red, Green, Blue;

void setup() {
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(50);
}

void loop() {
  // send data only when you receive data:
  while(Serial.available()){
    delay(20);
    //reads only one byte at a time and records it into the string variable
    char c = Serial.read();
    readString += c;};

  // finding the index points to create the substrings of data 

  for (int i=0; i< readString.length();i++){
    if (readString[i]=='R'){
      R_index = i;
      digitalWrite(10,HIGH);
      };
    if (readString[i]=='G'){
      G_index = i;
      };
    if (readString[i]=='B'){
      B_index = i;
      };
    }
    
  // extracting the data from the substring of data 
  // converting extracted string data into integers 
  Red = readString.substring(R_index + 1, G_index);
  Green = readString.substring(G_index + 1, B_index);
  Blue = readString.substring(B_index + 1, readString.length());

  EVERY_N_MILLISECONDS(20){
  fill_solid(leds, NUM_LEDS, CRGB(Red.toInt(), Green.toInt(), Blue.toInt()));
  FastLED.show();}
  
}
