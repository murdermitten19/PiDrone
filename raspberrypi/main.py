import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pin number
GPIO.setmode(GPIO.BOARD)
GPIO_PIN = 35

# Set PWM parameters
frequency = 100  # 100 Hz frequency
duty_cycle = 0    # Start with 0% duty cycle

# Setup the GPIO pin for PWM
GPIO.setup(GPIO_PIN, GPIO.OUT)
pwm = GPIO.PWM(GPIO_PIN, frequency)
pwm.start(duty_cycle)

try:
    while True:
        # Vary the duty cycle from 0 to 100 in steps of 5
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            print("Duty Cycle:", dc)
            time.sleep(0.5)  # Change every 0.5 seconds

        # Reverse the direction
        for dc in range(100, -1, -5):
            pwm.ChangeDutyCycle(dc)
            print("Duty Cycle:", dc)
            time.sleep(0.1)  # Change every 0.5 seconds

except KeyboardInterrupt:
    pass

# Clean up
pwm.stop()
GPIO.cleanup()