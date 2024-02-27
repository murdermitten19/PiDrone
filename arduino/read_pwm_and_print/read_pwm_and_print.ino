#include <Servo.h>

const int signalinfrompi1 = 2; // Pin for signal input from Pi 1
const int signalinfrompi2 = 4; // Pin for signal input from Pi 2
const int signalinfrompi3 = 7; // Pin for signal input from Pi 3
const int signalinfrompi4 = 8; // Pin for signal input from Pi 4

int infrompilow1 = 0; // Low value of input from Pi 1
int infrompilow2 = 0; // Low value of input from Pi 2
int infrompilow3 = 0; // Low value of input from Pi 3
int infrompilow4 = 0; // Low value of input from Pi 4

const int ESC_PIN_1 = 3; // Pin for ESC 1
const int ESC_PIN_2 = 5; // Pin for ESC 2
const int ESC_PIN_3 = 6; // Pin for ESC 3
const int ESC_PIN_4 = 9; // Pin for ESC 4

const int THROTTLE_MIN = 1000; // Minimum throttle value for ESCs
const int THROTTLE_FULL_MAX = 2000; // Maximum throttle value for full power
const int THROTTLE_MAX = 1500; // Maximum throttle value

int pitopwm1 = 0; // PWM value calculated from input of Pi 1
int pitopwm2 = 0; // PWM value calculated from input of Pi 2
int pitopwm3 = 0; // PWM value calculated from input of Pi 3
int pitopwm4 = 0; // PWM value calculated from input of Pi 4

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
  delay(2000); // Wait for 2 seconds

  
  Serial.begin(10000);
}

void loop() {

  unsigned long infrompi1 = pulseIn(signalinfrompi1, HIGH, 500UL);
  unsigned long infrompi2 = pulseIn(signalinfrompi2, HIGH, 500UL);
  unsigned long infrompi3 = pulseIn(signalinfrompi3, HIGH, 500UL);
  unsigned long infrompi4 = pulseIn(signalinfrompi4, HIGH, 500UL);



  pitopwm1 = map(infrompi1, 0, 10000, 1000, 1300);
  pitopwm1 = map(infrompi2, 0, 10000, 1000, 1300);
  pitopwm1 = map(infrompi3, 0, 10000, 1000, 1300);
  pitopwm1 = map(infrompi4, 0, 10000, 1000, 1300);


  esc1.writeMicroseconds(pitopwm1);
  esc2.writeMicroseconds(pitopwm2);
  esc3.writeMicroseconds(pitopwm3);
  esc4.writeMicroseconds(pitopwm4);


}






