#include <Servo.h>

const int signalinfrompi1 = 2; // Pin for signal input from Pi 1
const int signalinfrompi2 = 4; // Pin for signal input from Pi 2
const int signalinfrompi3 = 7; // Pin for signal input from Pi 3
const int signalinfrompi4 = 8; // Pin for signal input from Pi 4

int infrompihigh1 = 0; // High value of input from Pi 1
int infrompihigh2 = 0; // High value of input from Pi 2
int infrompihigh3 = 0; // High value of input from Pi 3
int infrompihigh4 = 0; // High value of input from Pi 4

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

  // int infrompi1 = pulseIn(signalinfrompi1, HIGH, 50000UL);
  // int infrompi2 = pulseIn(signalinfrompi2, HIGH, 50000UL);
  // int infrompi3 = pulseIn(signalinfrompi3, HIGH, 50000UL);
  // int infrompi4 = pulseIn(signalinfrompi4, HIGH, 50000UL);

  // int infrompi1 = pulseIn(signalinfrompi1, LOW, 50000UL);
  // int infrompi2 = pulseIn(signalinfrompi2, LOW, 50000UL);
  // int infrompi3 = pulseIn(signalinfrompi3, LOW, 50000UL);
  // int infrompi4 = pulseIn(signalinfrompi4, LOW, 50000UL);






  // pitopwm1 = map(infrompi1, 0, 10000, 1000, 1300);
  // pitopwm1 = map(infrompi2, 0, 10000, 1000, 1300);
  // pitopwm1 = map(infrompi3, 0, 10000, 1000, 1300);
  // pitopwm1 = map(infrompi4, 0, 10000, 1000, 1300);


  pitopwm1 = infrompi(signalinfrompi1);
  pitopwm2 = infrompi(signalinfrompi2);
  pitopwm3 = infrompi(signalinfrompi3);
  pitopwm4 = infrompi(signalinfrompi4);

  infrompihigh1 = map(pitopwm1, 0, 100, 1000, 1300);
  infrompihigh2 = map(pitopwm2, 0, 100, 1000, 1300);
  infrompihigh3 = map(pitopwm3, 0, 100, 1000, 1300);
  infrompihigh4 = map(pitopwm4, 0, 100, 1000, 1300);

  esc1.writeMicroseconds(infrompihigh1);
  esc2.writeMicroseconds(infrompihigh2);
  esc3.writeMicroseconds(infrompihigh3);
  esc4.writeMicroseconds(infrompihigh4);


}


/**
 * Reads the input value from the specified pin and returns it as a byte.
 * 
 * @param pin The pin number to read from.
 * @return The input value read from the pin as a byte.
 */
byte infrompi(byte pin)
{
  unsigned long highTime = pulseIn(pin, HIGH, 300UL);
  unsigned long lowTime = pulseIn(pin, LOW, 300UL);

  if (highTime == 0 || lowTime == 0)
    return digitalRead(pin) ? 100 : 0;

  return (100 * highTime) / (highTime + lowTime);
}







