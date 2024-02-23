# import socket

# # Server configuration
# HOST = '0.0.0.0'  # Listen on all network interfaces
# PORT = 12345  # Choose a port number

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the host and port
# server_socket.bind((HOST, PORT))

# # Listen for incoming connections
# server_socket.listen()

# print("Server is listening...")

# while True:
#     # Wait for a connection
#     client_socket, address = server_socket.accept()
#     print(f"Connection from {address}")

#     try:
#         while True:
#             # Receive data from the client
#             received_data = client_socket.recv(1024).decode().strip()
#             if not received_data:
#                 break  # No more data, end the loop
            
#             # Split the received message by comma
#             values = received_data.split(',')
            
#             # Ensure there are exactly 4 values
#             if len(values) != 4:
#                 print("Invalid number of motor values received")
#                 break
            
#             # Convert values to integers and store in separate variables
#             motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)
            
#             print("Received Motor Values:")
#             print("Motor 1:", motor_value1)
#             print("Motor 2:", motor_value2)
#             print("Motor 3:", motor_value3)
#             print("Motor 4:", motor_value4)

#     except Exception as e:
#         print("Error receiving data:", e)
    
#     # Close the connection
#     client_socket.close()



# import socket
# import RPi.GPIO as GPIO

# # Server configuration
# HOST = '0.0.0.0'  # Listen on all network interfaces
# PORT = 12345  # Choose a port number

# # GPIO pins for PWM
# GPIO.setmode(GPIO.BOARD)
# MOTOR_PINS = [32, 33, 12, 35]

# # Initialize PWM for each motor pin
# pwm_motors = [GPIO.PWM(pin, 100) for pin in MOTOR_PINS]
# for pwm in pwm_motors:
#     pwm.start(0)  # Start with duty cycle of 0

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Bind the socket to the host and port
# server_socket.bind((HOST, PORT))

# # Listen for incoming connections
# server_socket.listen()

# print("Server is listening...")

# while True:
#     # Wait for a connection
#     client_socket, address = server_socket.accept()
#     print(f"Connection from {address}")

#     try:
#         while True:
#             # Receive data from the client
#             received_data = client_socket.recv(1024).decode().strip()
#             if not received_data:
#                 break  # No more data, end the loop
            
#             # Split the received message by comma
#             values = received_data.split(',')
            
#             # Ensure there are exactly 4 values
#             if len(values) != 4:
#                 print("Invalid number of motor values received")
#                 break
            
#             # Convert values to integers and store in separate variables
#             motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)
            
#             # Convert motor values to percentage (PWM duty cycle)
#             pwm_values = [motor_value1, motor_value2, motor_value3, motor_value4]
#             pwm_values = [min(max(val, 0), 100) for val in pwm_values]  # Ensure values are between 0 and 100
            
#             # Update PWM duty cycles
#             for pwm, value in zip(pwm_motors, pwm_values):
#                 pwm.ChangeDutyCycle(value)
            
#             print("Received Motor Values (PWM %):")
#             print("Motor 1:", pwm_values[0])
#             print("Motor 2:", pwm_values[1])
#             print("Motor 3:", pwm_values[2])
#             print("Motor 4:", pwm_values[3])

#     except Exception as e:
#         print("Error receiving data:", e)
    
#     # Close the connection
#     client_socket.close()

# # Cleanup GPIO
# for pwm in pwm_motors:
#     pwm.stop()
# GPIO.cleanup()



import socket
import RPi.GPIO as GPIO

# Server configuration
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 12345  # Choose a port number

# GPIO pins for PWM
GPIO.setmode(GPIO.BOARD)
MOTOR_PINS = [32, 33, 12, 35]

# Initialize PWM for each motor pin
for pin in MOTOR_PINS:
    GPIO.setup(pin, GPIO.OUT)  # Set up as output
    GPIO.output(pin, GPIO.LOW)  # Start with output low

pwm_motors = [GPIO.PWM(pin, 100) for pin in MOTOR_PINS]
for pwm in pwm_motors:
    pwm.start(0)  # Start with duty cycle of 0

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print("Server is listening...")

while True:
    # Wait for a connection
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    try:
        while True:
            # Receive data from the client
            received_data = client_socket.recv(1024).decode().strip()
            if not received_data:
                break  # No more data, end the loop
            
            # Split the received message by comma
            values = received_data.split(',')
            
            # Ensure there are exactly 4 values
            if len(values) != 4:
                print("Invalid number of motor values received")
                break
            
            # Convert values to integers and store in separate variables
            motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)
            
            # Convert motor values to percentage (PWM duty cycle)
            pwm_values = [motor_value1, motor_value2, motor_value3, motor_value4]
            pwm_values = [min(max(val, 0), 100) for val in pwm_values]  # Ensure values are between 0 and 100
            
            # Update PWM duty cycles
            for pwm, value in zip(pwm_motors, pwm_values):
                pwm.ChangeDutyCycle(value)
            
            print("Received Motor Values (PWM %):")
            print("Motor 1:", pwm_values[0])
            print("Motor 2:", pwm_values[1])
            print("Motor 3:", pwm_values[2])
            print("Motor 4:", pwm_values[3])

    except Exception as e:
        print("Error receiving data:", e)
    
    # Close the connection
    client_socket.close()

# Cleanup GPIO
for pwm in pwm_motors:
    pwm.stop()
GPIO.cleanup()
