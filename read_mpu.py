import socket
import smbus
import time

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




def read_raw_data(addr):
        high = MPU.read_byte_data(Device_Address, addr)
        low = MPU.read_byte_data(Device_Address, addr)
    
        value = ((high << 8) | low)
        
        if(value > 32768):
                value = value - 65536

        time.sleep(0.02)
        return value
    


def hover():
    read_raw_data()






# client_socket, address = server_socket.accept()
# print(f"Verbindung von {address}")


"""
FYI
Ax = links(-)/rechts(+)
Ay = vorne(+)/hinten(-)
Az = nur gott weiß

"""



while True:

    acc_x = read_raw_data(ACCEL_XOUT)
    acc_y = read_raw_data(ACCEL_YOUT)
    acc_z = read_raw_data(ACCEL_ZOUT)

    Ax = acc_x/16384.0 - 0.03
    Ay = acc_y/16384.0 + 0.03
    Az = acc_z/16384.0


  
    # print ("\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
       
    # received_data = client_socket.recv(1024).decode().strip()
    
    # received_data = "w-"
    
    if received_data in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-'] and Ax < 0.03 and Ax > -0.03 and Ay < 0.03 and Ay > -0.03:
       print("staright")
    else:
       print("tilted")


#-0.07
