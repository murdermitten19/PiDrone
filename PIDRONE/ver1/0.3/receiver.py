import socket
import smbus
import pigpio as GPIO
import time

# Definieren der Host- und Portvariablen
HOST = '0.0.0.0'
PORT = 12345


HOVER_SPEED = 145
STARTUP_SPEED = 145


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
MOTOR_3 = 13
MOTOR_4 = 19

motor_value1 = 0
motor_value2 = 0
motor_value3 = 0
motor_value4 = 0

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

time.sleep(5)

PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, STARTUP_SPEED - 20)
PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, STARTUP_SPEED + 10)
PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, STARTUP_SPEED - 21)
PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, STARTUP_SPEED + 12)



def read_raw_data(addr):
        high = MPU.read_byte_data(Device_Address, addr)
        low = MPU.read_byte_data(Device_Address, addr)
    
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

    return motor_value1, motor_value2, motor_value3, motor_value4


# client_socket, address = server_socket.accept()
# print(f"Verbindung von {address}")

client_socket, address = server_socket.accept()










while True:

    # print ("\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	

    acc_x = read_raw_data(ACCEL_XOUT)
    acc_y = read_raw_data(ACCEL_YOUT)
    acc_z = read_raw_data(ACCEL_ZOUT)

    Ax = acc_x/16384.0 - 0.03
    Ay = acc_y/16384.0 + 0.03
    Az = acc_z/16384.0
 
    received_data = client_socket.recv(1024).decode().strip()
    if not received_data: continue
    if received_data not in ['w+', 'a+', 's+', 'd+', '8+', '4+', '5+', '6+', 'w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:
        print("Ungültiges Datenformat erhalten.")
        continue
    else:
        convert_Data(received_data)




    """
    FYI
    Ax = links(-)/rechts(+)
    Ay = vorne(+)/hinten(-)
    Az = nur gott weiß

    """

    
    if received_data in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:

        if Ax < 0.03 and Ax > -0.03 and Ay < 0.03 and Ay > -0.03:
            print("hovering")

        else:

            if Ax > 0.03:
                print("Tilt to the right")
                # Balance to the left
                received_data = "a+"
                convert_Data(received_data)
            elif Ax < -0.03:
                print("Tilt to the left")
                #Balance to the right
                received_data = "d+"
                convert_Data(received_data)
            if Ay > 0.03:
                print("Tilt to the front")
                #Balance to the back
                received_data = "s+"
                convert_Data(received_data)
            elif Ay < -0.03:
                print("Tilt to the back")
                #Balance to the front
                received_data = "w+"
                convert_Data(received_data)
    





    elif received_data in ['w+', 'a+', 's+', 'd+', '8+', '4+', '5+', '6+']:
        print("key pressed")





# and Ax < 0.03 and Ax > -0.03 and Ay < 0.03 and Ay > -0.03