import socket
import pigpio as GPIO

HOST = '0.0.0.0'
PORT = 12345

MOTOR_1 = 18
MOTOR_2 = 12
MOTOR_3 = 19
MOTOR_4 = 13


PWM_MOTOR_1 = GPIO.pi()
PWM_MOTOR_2 = GPIO.pi()
PWM_MOTOR_3 = GPIO.pi()
PWM_MOTOR_4 = GPIO.pi()

PWM_MOTOR_1.set_PWM_frequency(MOTOR_1, 500)
PWM_MOTOR_2.set_PWM_frequency(MOTOR_2, 500)
PWM_MOTOR_3.set_PWM_frequency(MOTOR_3, 500)
PWM_MOTOR_4.set_PWM_frequency(MOTOR_4, 500)

PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, 0)
PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, 0)
PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, 0)
PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, 0)



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is listening...")

while True:
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    try:
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


                PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1)
                PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2)
                PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3)
                PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4)


                print("Received Motor Values (PWM %):")
                print("Motor 1:", motor_value1)
                print("Motor 2:", motor_value2)
                print("Motor 3:", motor_value3)
                print("Motor 4:", motor_value4)

                
            

    except Exception as e:
        print("Error receiving data:", e)
    
    client_socket.close()

# Stop PWM and clean up GPIO
    PWM_MOTOR_1.stop()
    PWM_MOTOR_2.stop()
    PWM_MOTOR_3.stop()
    PWM_MOTOR_4.stop()

    GPIO.stop()
