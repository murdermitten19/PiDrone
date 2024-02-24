#include <Servo.h>

int infrompilow1 = 0;
int infrompilow2 = 0;
int infrompilow3 = 0;
int infrompilow4 = 0;



const int ESC_PIN_1 = 3;
const int ESC_PIN_2 = 5;
const int ESC_PIN_3 = 6;
const int ESC_PIN_4 = 9;

const int THROTTLE_MIN = 1000;
const int THROTTLE_FULL_MAX = 2000;
const int THROTTLE_MAX = 1500;

int pitopwm1 = 0;
int pitopwm2 = 0;
int pitopwm3 = 0;
int pitopwm4 = 0;

Servo motA;
char data;

Servo esc1, esc2, esc3, esc4;

const int pinfrompi1 = 2;
const int pinfrompi2 = 4;
const int pinfrompi3 = 7;
const int pinfrompi4 = 8;

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

  unsigned long pulsein1 = pulseIn(pinfrompi1, HIGH);
  unsigned long pulsein2 = pulseIn(pinfrompi2, HIGH);
  unsigned long pulsein3 = pulseIn(pinfrompi3, HIGH);
  unsigned long pulsein4 = pulseIn(pinfrompi4, HIGH);

  unsigned long mappedpulse1 = map(pulsein1, 0, 10000, 1000, 1300);
  unsigned long mappedpulse2 = map(pulsein2, 0, 10000, 1000, 1300);
  unsigned long mappedpulse3 = map(pulsein3, 0, 10000, 1000, 1300);
  unsigned long mappedpulse4 = map(pulsein4, 0, 10000, 1000, 1300);

  Serial.println(mappedpulse1);
  Serial.println(mappedpulse2);
  Serial.println(mappedpulse3);
  Serial.println(mappedpulse4);

}



