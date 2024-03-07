import RPi.GPIO as GPIO
import time

# GPIO Pin for the ESC
ESC_PIN = 12

# ESC Constants
ESC_MIN = 1000  # 1ms
ESC_MAX = 1300  # 2ms

# PWM Frequency
PWM_FREQ = 1000  # Hz

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def setup_esc():
    GPIO.setup(ESC_PIN, GPIO.OUT)
    pwm = GPIO.PWM(ESC_PIN, PWM_FREQ)
    pwm.start(0)  # Start with duty cycle 0
    time.sleep(2)  # Delay for ESC to initialize

def set_esc_speed(speed):
    duty = speed_to_duty(speed)
    pwm.ChangeDutyCycle(duty)

def speed_to_duty(speed):
    # Convert speed (1000-2000) to duty cycle (0-100)
    duty = (speed - ESC_MIN) / (ESC_MAX - ESC_MIN) * 100
    return duty

def disarm_esc():
    pwm.stop()

def stop_esc():
    pwm.ChangeDutyCycle(0)

def main():
    try:
        setup_esc()

        while True:
            print("Select Mode:")
            print("1. Set Speed")
            print("2. Stop")
            print("3. Exit")

            mode = input("Enter mode: ")

            if mode == '1':
                speed = int(input("Enter speed (1000-2000): "))
                set_esc_speed(speed)
            elif mode == '2':
                stop_esc()
            elif mode == '3':
                break
            else:
                print("Invalid mode. Try again.")

    except KeyboardInterrupt:
        print("\nExiting program...")
    finally:
        disarm_esc()
        GPIO.cleanup()

if __name__ == "__main__":
    main()
