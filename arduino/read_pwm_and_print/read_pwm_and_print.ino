const int pwmPin = 2; // Change this to the pin connected to Raspberry Pi PWM
int dutyCycle = 0;

#include <Servo.h>

// Define Pins for ESCs
#define ESC_PIN_1 3
#define ESC_PIN_2 5
#define ESC_PIN_3 6
#define ESC_PIN_4 9

// Define throttle values (adjust as needed)
#define THROTTLE_MIN 1000
#define THROTTLE_MAX 2000

// Create servo objects for each ESC
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
  unsigned long pulseWidth = pulseIn(pwmPin, HIGH);  // Measure pulse width when signal is HIGH

  // Calculate duty cycle as a percentage
  int dutyCycle = map(pulseWidth, 0, 10000, 0, 100);  // Assuming a typical servo range of 1000-2000 microseconds

  // Print the pulse width and duty cycle
  Serial.print("Pulse Width (microseconds): ");
  Serial.print(pulseWidth);
  Serial.print("    Duty Cycle (%): ");
  Serial.println(dutyCycle);

  delay(100);  // Delay for stability, adjust as needed
}


