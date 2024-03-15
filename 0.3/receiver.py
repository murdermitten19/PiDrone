# import socket
# import pigpio as GPIO
import time

# # Definieren der Host- und Portvariablen
# HOST = '0.0.0.0'
# PORT = 12345

# # Definieren der Motorvariablen
# MOTOR_1 = 18
# MOTOR_2 = 12
# MOTOR_3 = 19
# MOTOR_4 = 13

# # Erstellen Sie PWM-Instanzen für jeden Motor
# PWM_MOTOR_1 = GPIO.pi()
# PWM_MOTOR_2 = GPIO.pi()
# PWM_MOTOR_3 = GPIO.pi()
# PWM_MOTOR_4 = GPIO.pi()

# # Setzen der PWM-Frequenz für jeden Motor
# PWM_MOTOR_1.set_PWM_frequency(MOTOR_1, 500)
# PWM_MOTOR_2.set_PWM_frequency(MOTOR_2, 500)
# PWM_MOTOR_3.set_PWM_frequency(MOTOR_3, 500)
# PWM_MOTOR_4.set_PWM_frequency(MOTOR_4, 500)

# # Setzen des PWM-Dutycycles für jeden Motor auf 0
# PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, 0)
# PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, 0)
# PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, 0)
# PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, 0)

# # Erstellen des Server-Socket
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind((HOST, PORT))
# server_socket.listen()

# print("Server hört zu...")


# # Main loop
# while True:
#     # Verbindung von einem Client akzeptieren
#     client_socket, address = server_socket.accept()
#     print(f"Verbindung von {address}")

#     try:
#         while True:
#             received_data = client_socket.recv(1024).decode().strip()
#             if not received_data:
#                 break
            
#             # Teilen der empfangenen Daten in 4 Werte
#             values = received_data.split(',')

#             # Überprüfung empfangener Daten
#             if len(values) != 4:
#                 print("Ungültiges Datenformat erhalten. Erwartet wurden 4 durch Komma getrennte Werte.")
#                 continue

#             else:
#                 print(values)
#                 motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)

#                 # Setzen Sie den PWM-Tastverhältniszyklus für jeden Motor auf den empfangenen Wert
#                 PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1)
#                 PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2)
#                 PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3)
#                 PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4)

#                 # print("Empfangene Motorwerte (PWM %):")
#                 # print("Motor 1:", motor_value1)
#                 # print("Motor 2:", motor_value2)
#                 # print("Motor 3:", motor_value3)
#                 # print("Motor 4:", motor_value4)

#     # Fehlerbehandlung
#     except Exception as e:
#         print("Fehler beim Empfangen von Daten:", e)
 
#     # Schließen der Verbindung zum Client
#     client_socket.close()

# # Stoppen Sie PWM und bereinigen Sie GPIO
#     PWM_MOTOR_1.stop()
#     PWM_MOTOR_2.stop()
#     PWM_MOTOR_3.stop()
#     PWM_MOTOR_4.stop()

#     GPIO.stop()


"""
	Simple code to read data from the temperature sensor, accelerometer and gyroscope sensors
	inside of MPU6050

	The propertie whoami provides the i2c address of the device
"""




# from mpu6050 import mpu6050
# import time
# mpu = mpu6050(0x68)

# while True:
#     print("Temp : "+str(mpu.get_temp()))
#     print()

#     gyro_data = mpu.get_gyro_data()
#     print("Gyro X : "+str(gyro_data['x']))
#     print("Gyro Y : "+str(gyro_data['y']))
#     print("Gyro Z : "+str(gyro_data['z']))

#     time.sleep(1)




import RPi.GPIO as GPIO
import smbus 
from time import sleep

# Setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Set the servo motor pin as output pin
GPIO.setup(4,GPIO.OUT)

pwm = GPIO.PWM(4,50)
pwm.start(0)

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT  = 0x43
GYRO_YOUT  = 0x45
GYRO_ZOUT  = 0x47


bus = smbus.SMBus(1) # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68 # MPU6050 device address

def angle(Angle):
    duty = Angle / 18 + 2
    GPIO.output(4,True)
    pwm.ChangeDutyCycle(duty)
#     sleep(1)
    GPIO.output(4,False)
#     pwm.ChangeDutyCycle(0)
    
def setAngle():
    angle(90)

def MPU_Init():
    
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)

    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 0)

    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
    
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
    

MPU_Init()

while True:
    #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT)
    acc_y = read_raw_data(ACCEL_YOUT)
    acc_z = read_raw_data(ACCEL_ZOUT)

    #Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT)
    gyro_y = read_raw_data(GYRO_YOUT)
    gyro_z = read_raw_data(GYRO_ZOUT)

    Ax = acc_x/16384.0
    Ay = acc_y/16384.0 
    Az = acc_z/16384.0

    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0

# Uncomment below line to see the Accelerometer and Gyroscope values   
#    print ("Gx=%.2f" %Gx, u'\u00b0'+ "/s", "\tGy=%.2f" %Gy, u'\u00b0'+ "/s", "\tGz=%.2f" %Gz, u'\u00b0'+ "/s", "\tAx=%.2f g" %Ax, "\tAy=%.2f g" %Ay, "\tAz=%.2f g" %Az) 	
       
    in_min = 1
    in_max = -1
    out_min = 0
    out_max = 180
    
    setAngle() # Use this function to set the servo motor point
    
    # Convert accelerometer Y axis values from 0 to 180   
    value = (Ay - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    value = int(value)
    print(value)
    if value >= 0 and value <= 180:
        # Write these values on the servo motor
#         angle(value) # Rotate the servo motor using the sensor values
        sleep(0.08)
        