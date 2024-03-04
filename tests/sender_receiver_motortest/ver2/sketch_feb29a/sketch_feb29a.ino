#include <Servo.h>


const int signalinfrompi1 = 2; // Pin for signal input from Pi 1
const int signalinfrompi2 = 4; // Pin for signal input from Pi 2
const int signalinfrompi3 = 7; // Pin for signal input from Pi 3
const int signalinfrompi4 = 8; // Pin for signal input from Pi 4

const int ESC_PIN_1 = 3; // Pin for ESC 1
const int ESC_PIN_2 = 5; // Pin for ESC 2
const int ESC_PIN_3 = 6; // Pin for ESC 3
const int ESC_PIN_4 = 9; // Pin for ESC 4

const int THROTTLE_MIN = 1000; // Minimum throttle value for ESCs
const int THROTTLE_FULL_MAX = 2000; // Maximum throttle value for full power
const int THROTTLE_MAX = 1300; // Maximum throttle value

Servo motA; // Placeholder for motor A
char data; // Placeholder for data

Servo esc1, esc2, esc3, esc4; // ESC objects for each motor

void setup() {

  esc1.attach(ESC_PIN_1);
  esc2.attach(ESC_PIN_2);
  esc3.attach(ESC_PIN_3);
  esc4.attach(ESC_PIN_4);
  
  // Send minimum throttle to calibrate ESCs
  esc1.writeMicroseconds(THROTTLE_MIN);
  esc2.writeMicroseconds(THROTTLE_MIN);
  esc3.writeMicroseconds(THROTTLE_MIN);
  esc4.writeMicroseconds(THROTTLE_MIN);
  delay(5000); // Wait for 5 seconds

  
  Serial.begin(10000);
}

void loop() {

  unsigned long infrompi1 = pulseIn(signalinfrompi1, HIGH, 500UL);
  unsigned long infrompi2 = pulseIn(signalinfrompi2, HIGH, 500UL);
  unsigned long infrompi3 = pulseIn(signalinfrompi3, HIGH, 500UL);
  unsigned long infrompi4 = pulseIn(signalinfrompi4, HIGH, 500UL);

  unsigned long pitopwm1 = map(infrompi1, 0, 100, 1099, 1300);
  unsigned long pitopwm2 = map(infrompi2, 0, 100, 1099, 1300);
  unsigned long pitopwm3 = map(infrompi3, 0, 100, 1099, 1300);
  unsigned long pitopwm4 = map(infrompi4, 0, 100, 1099, 1300);


  Serial.println(pitopwm1);
  Serial.println(pitopwm2);
  Serial.println(pitopwm3);
  Serial.println(pitopwm4);

  esc1.writeMicroseconds(pitopwm1);
  esc2.writeMicroseconds(pitopwm2);
  esc3.writeMicroseconds(pitopwm3);
  esc4.writeMicroseconds(pitopwm4);

}






