import socket
import RPi.GPIO as GPIO
import json

HOST = '0.0.0.0'
PORT = 12345

GPIO.setmode(GPIO.BOARD)
MOTOR_PINS = [32, 33, 12, 35]


for pin in MOTOR_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

pwm_motors = [GPIO.PWM(pin, 100) for pin in MOTOR_PINS]
for pwm in pwm_motors:
    pwm.start(0)


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
                print("Invalid number of motor values received")
                break
            
            motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)
            
            pwm_values = [motor_value1, motor_value2, motor_value3, motor_value4]
            pwm_values = [min(max(val, 0), 100) for val in pwm_values]
            
            for pwm, value in zip(pwm_motors, pwm_values):
                pwm.ChangeDutyCycle(value)
            
            print("Received Motor Values (PWM %):")
            print("Motor 1:", pwm_values[0])
            print("Motor 2:", pwm_values[1])
            print("Motor 3:", pwm_values[2])
            print("Motor 4:", pwm_values[3])

            # json_data = {
            #     "pwm_value0": pwm_values[0],
            #     "pwm_value1": pwm_values[1],
            #     "pwm_value2": pwm_values[2],
            #     "pwm_value3": pwm_values[3]
            # }

            # # Load the existing json file
            # with open('data.json', 'r') as file:
            #     existing_data = json.load(file)

            # # Update the pwm values in the existing json data
            # existing_data.update(json_data)

            # # Save the updated json data back to the file
            # with open('data.json', 'w') as file:
            #     json.dump(existing_data, file)



    except Exception as e:
        print("Error receiving data:", e)
    
    client_socket.close()

for pwm in pwm_motors:
    pwm.stop()
GPIO.cleanup()
