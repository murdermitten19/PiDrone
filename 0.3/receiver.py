import socket
import smbus
import pigpio as GPIO

# Definieren der Host- und Portvariablen
HOST = '0.0.0.0'
PORT = 12345

value = 0
received_data = "w-"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("server is listening on", HOST, PORT)

MPU = smbus.SMBus(1)
Device_Address = 0x68

ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT  = 0x43
GYRO_YOUT  = 0x45
GYRO_ZOUT  = 0x47

MOTOR_1 = 18
MOTOR_2 = 12
MOTOR_3 = 19
MOTOR_4 = 13

HOVER_SPEED = 130


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



def read_raw_data(addr):
        high = MPU.read_byte_data(Device_Address, addr)
        low = MPU.read_byte_data(Device_Address, addr+1)
    
        value = ((high << 8) | low)
        
        if(value > 32768):
                value = value - 65536
        return value
    



def hover():
    read_raw_data()


def convert_Data(received_data):
    if received_data == "w+":
        motor_value1 = HOVER_SPEED + 3
        motor_value2 = HOVER_SPEED + 3
        motor_value3 = HOVER_SPEED + 3
        motor_value4 = HOVER_SPEED + 3
    elif received_data == "a+":
        motor_value1 = HOVER_SPEED - 3
        motor_value2 = HOVER_SPEED + 3
        motor_value3 = HOVER_SPEED - 3
        motor_value4 = HOVER_SPEED + 3
    elif received_data == "s+":
        motor_value1 = HOVER_SPEED - 3
        motor_value2 = HOVER_SPEED - 3
        motor_value3 = HOVER_SPEED - 3
        motor_value4 = HOVER_SPEED - 3
    elif received_data == "d+":
        motor_value1 = HOVER_SPEED + 3 
        motor_value2 = HOVER_SPEED - 3
        motor_value3 = HOVER_SPEED + 3
        motor_value4 = HOVER_SPEED - 3
    elif received_data == "8+":
        motor_value1 = HOVER_SPEED -3
        motor_value2 = HOVER_SPEED -3
        motor_value3 = HOVER_SPEED +3 
        motor_value4 = HOVER_SPEED +3
    elif received_data == "4+":
        motor_value1 = HOVER_SPEED -3
        motor_value2 = HOVER_SPEED +3
        motor_value3 = HOVER_SPEED +3
        motor_value4 = HOVER_SPEED -3
    elif received_data == "5+":
        motor_value1 = HOVER_SPEED +3
        motor_value2 = HOVER_SPEED +3
        motor_value3 = HOVER_SPEED -3
        motor_value4 = HOVER_SPEED -3
    elif received_data == "6+":
        motor_value1 = HOVER_SPEED +3
        motor_value2 = HOVER_SPEED -3
        motor_value3 = HOVER_SPEED -3
        motor_value4 = HOVER_SPEED +3
    elif received_data == "w-" or "a-" or "s-" or "d-" or "8-" or "4-" or "5-" or "6-":
        motor_value1 = HOVER_SPEED
        motor_value2 = HOVER_SPEED
        motor_value3 = HOVER_SPEED
        motor_value4 = HOVER_SPEED


# client_socket, address = server_socket.accept()
# print(f"Verbindung von {address}")

client_socket, address = server_socket.accept()

while True:

    acc_x = read_raw_data(ACCEL_XOUT)
    acc_y = read_raw_data(ACCEL_YOUT)
    acc_z = read_raw_data(ACCEL_ZOUT)

    Ax = acc_x/16384.0
    Ay = acc_y/16384.0 
    Az = acc_z/16384.0

    # print ("\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
  

       
    received_data = client_socket.recv(1024).decode().strip()
    if received_data not in ['w+', 'a+', 's+', 'd+', '8+', '4+', '5+', '6+', 'w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:
        print("Ungültiges Datenformat erhalten.")
        continue
    else:
        convert_Data(received_data)

    
    if received_data in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-'] and Ax < 0.06 and Ax > 0.02 and Ay <0.01 and Ay > -0.06:
    # Unbalanced Hovering
            PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1)
            PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2)
            PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3)
            PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4)
    
    elif received_data in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:
    # Balanced Hovering
    
    else:
    # Controlled Flight
         print("a")

