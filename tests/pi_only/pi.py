import socket
import RPi.GPIO as GPIO
import time

HOST = '0.0.0.0'
PORT = 12345

GPIO.setmode(GPIO.BOARD)

MOTOR_PINS_1 = 12
# MOTOR_PINS_2 = 33
# MOTOR_PINS_3 = 12
# MOTOR_PINS_4 = 35

GPIO.setup(MOTOR_PINS_1, GPIO.OUT)
# GPIO.setup(MOTOR_PINS_2,GPIO.OUT)
# GPIO.setup(MOTOR_PINS_3,GPIO.OUT)
# GPIO.setup(MOTOR_PINS_4,GPIO.OUT)

PWM_MOTOR_1 = GPIO.PWM(MOTOR_PINS_1, 2000)
# PWM_MOTOR_2 = GPIO.PWM(MOTOR_PINS_2,1000)
# PWM_MOTOR_3 = GPIO.PWM(MOTOR_PINS_3,1000)
# PWM_MOTOR_4 = GPIO.PWM(MOTOR_PINS_4,1000)

PWM_MOTOR_1.start(0)
# PWM_MOTOR_2.start(0)
# PWM_MOTOR_3.start(0)
# PWM_MOTOR_4.start(0)



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is listening...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    try:
        
        PWM_MOTOR_1.ChangeDutyCycle(0)
        # PWM_MOTOR_2.ChangeDutyCycle(0)
        # PWM_MOTOR_3.ChangeDutyCycle(0)
        # PWM_MOTOR_4.ChangeDutyCycle(0)
        time.sleep(10)
        
        
        
        while True:
            received_data = client_socket.recv(1024).decode().strip()
            if not received_data:
                break
            
            values = received_data.split(',')
            
            if len(values) != 4:
                print("Received invalid data format. Expected 4 values separated by comma.")
                continue

            else:
                print(values)
                motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)

                print("Received Motor Values (PWM %):")
                print("Motor 1:", motor_value1)
                print("Motor 2:", motor_value2)
                print("Motor 3:", motor_value3)
                print("Motor 4:", motor_value4)

                PWM_MOTOR_1.ChangeDutyCycle(motor_value1)
                # PWM_MOTOR_2.ChangeDutyCycle(0)
                # PWM_MOTOR_3.ChangeDutyCycle(0)
                # PWM_MOTOR_4.ChangeDutyCycle(0)

                
            

    except Exception as e:
        print("Error receiving data:", e)
    
    client_socket.close()

# Stop PWM and clean up GPIO
    PWM_MOTOR_1.stop()
    # PWM_MOTOR_2.stop()
    # PWM_MOTOR_3.stop()
    # PWM_MOTOR_4.stop()

    GPIO.cleanup()
