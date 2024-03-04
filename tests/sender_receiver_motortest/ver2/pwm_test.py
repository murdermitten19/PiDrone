import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

MOTOR_PINS_1 = 32
MOTOR_PINS_2 = 33
MOTOR_PINS_3 = 12
MOTOR_PINS_4 = 35




GPIO.setup(MOTOR_PINS_1,GPIO.OUT)
GPIO.setup(MOTOR_PINS_2,GPIO.OUT)
GPIO.setup(MOTOR_PINS_3,GPIO.OUT)
GPIO.setup(MOTOR_PINS_4,GPIO.OUT)

PWM_MOTOR_1 = GPIO.PWM(MOTOR_PINS_1,1000)
PWM_MOTOR_2 = GPIO.PWM(MOTOR_PINS_2,1000)
PWM_MOTOR_3 = GPIO.PWM(MOTOR_PINS_3,1000)
PWM_MOTOR_4 = GPIO.PWM(MOTOR_PINS_4,1000)
try:
    while True:
        PWM_MOTOR_1.start(50)
        PWM_MOTOR_2.start(50)
        PWM_MOTOR_3.start(50)
        PWM_MOTOR_4.start(50)

except:
    KeyboardInterrupt()


    PWM_MOTOR_1.stop()
    PWM_MOTOR_2.stop()
    PWM_MOTOR_3.stop()
    PWM_MOTOR_4.stop()

    GPIO.cleanup()

