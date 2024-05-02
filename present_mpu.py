import smbus
import time

MPU = smbus.SMBus(1)
Device_Address = 0x68

ACCEL_XOUT = 0x3B
ACCEL_YOUT = 0x3D
ACCEL_ZOUT = 0x3F
GYRO_XOUT  = 0x43
GYRO_YOUT  = 0x45
GYRO_ZOUT  = 0x47

def read_raw_data(addr):
        global Device_Address, MPU
        high = MPU.read_byte_data(Device_Address, addr)
        low = MPU.read_byte_data(Device_Address, addr+1)
    
        value = ((high << 8) | low)
        
        if(value > 32768):
                value = value - 65536
        return value
    

while True:

    acc_x = read_raw_data(ACCEL_XOUT)
    acc_y = read_raw_data(ACCEL_YOUT)
    acc_z = read_raw_data(ACCEL_ZOUT)

    Ax = acc_x/16384.0 - 0.03
    Ay = acc_y/16384.0 + 0.03
    Az = acc_z/16384.0
        
    time.sleep(0.08)

    if Ax < 0.05 and Ax > -0.05 and Ay < 0.05 and Ay > -0.05:
        print("straight")

    else:


        if Ax > 0.05 and Ay > 0.05:
            print("Tilted to the front right")
            continue

        elif Ax > 0.05 and Ay < -0.05:
            print("Tilted to the back right")
            continue

        elif Ax < -0.05 and Ay > 0.05:
            print("Tilted to the front left")
            continue

        elif Ax < -0.05 and Ay < -0.05:
            print("Tilted to the back left")
            continue

        elif Ax > 0.05:
            print("Tilted to the right")
            continue

        elif Ax < -0.05:
            print("Tilted to the left")
            continue

        if Ay > 0.05:
            print("Tilted to the front")
            continue

        elif Ay < -0.05:
            print("Tilted to the back")
            continue

