#include <Servo.h>

const int pwmPin1 = 2;
const int pwmPin2 = 4;
const int pwmPin3 = 7;
const int pwmPin4 = 8;

const int ESC_PIN_1 = 3;
const int ESC_PIN_2 = 5;
const int ESC_PIN_3 = 6;
const int ESC_PIN_4 = 9;

const int THROTTLE_MIN = 1000;
const int THROTTLE_FULL_MAX = 2000;
const int THROTTLE_MAX = 1500;

int dutyCycle1 = 0;
int dutyCycle2 = 0;
int dutyCycle3 = 0;
int dutyCycle4 = 0;

int pitopwm1 = 0;
int pitopwm2 = 0;
int pitopwm3 = 0;
int pitopwm4 = 0;

Servo motA;
char data;

Servo esc1, esc2, esc3, esc4;



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

  
  Serial.begin(9600);
}

void loop() {
  unsigned long pulseWidth1 = pulseIn(pwmPin1, HIGH);
  int dutyCycle1 = map(pulseWidth1, 0, 10000, 0, 100);
  
  unsigned long pulseWidth2 = pulseIn(pwmPin2, HIGH);
  int dutyCycle2 = map(pulseWidth2, 0, 10000, 0, 100);
  
  unsigned long pulseWidth3 = pulseIn(pwmPin3, HIGH);
  int dutyCycle3 = map(pulseWidth3, 0, 10000, 0, 100);
  
  unsigned long pulseWidth4 = pulseIn(pwmPin4, HIGH);
  int dutyCycle4 = map(pulseWidth4, 0, 10000, 0, 100);

  // // Print the pulse width and duty cycle
  // Serial.print("Pulse Width 1 (microseconds): ");
  // Serial.print(pulseWidth1);
  // Serial.print("    Duty Cycle (%): ");
  // Serial.println(dutyCycle1);

  // Serial.print("Pulse Width 2 (microseconds): ");
  // Serial.print(pulseWidth2);
  // Serial.print("    Duty Cycle (%): ");
  // Serial.println(dutyCycle2);

  // Serial.print("Pulse Width 3 (microseconds): ");
  // Serial.print(pulseWidth3);
  // Serial.print("    Duty Cycle (%): ");
  // Serial.println(dutyCycle3);

  // Serial.print("Pulse Width 4 (microseconds): ");
  // Serial.print(pulseWidth4);
  // Serial.print("    Duty Cycle (%): ");
  // Serial.println(dutyCycle4);


  int pitopwm1 = map(dutyCycle1, 0, 100, 1000, 1300);
  int pitopwm2 = map(dutyCycle2, 0, 100, 1000, 1300);
  int pitopwm3 = map(dutyCycle3, 0, 100, 1000, 1300);
  int pitopwm4 = map(dutyCycle4, 0, 100, 1000, 1300);



  esc1.writeMicroseconds(pitopwm1);
  esc2.writeMicroseconds(pitopwm2);
  esc3.writeMicroseconds(pitopwm3);
  esc4.writeMicroseconds(pitopwm4);



  // delay(20);  // Delay for stability, adjust as needed
}


