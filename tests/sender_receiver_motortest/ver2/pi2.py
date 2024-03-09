import socket
import pigpio as GPIO
from mpu6050 import mpu6050
import time
import json

HOST = '0.0.0.0'
PORT = 12345

# Festlegen von Motorpins
MOTOR_1 = 12
MOTOR_2 = 13
MOTOR_3 = 18
MOTOR_4 = 19

# Initialisierung von PWM-Variabeln
PWM_MOTOR_1 = GPIO.pi()
PWM_MOTOR_2 = GPIO.pi()
PWM_MOTOR_3 = GPIO.pi()
PWM_MOTOR_4 = GPIO.pi()

# Initialisierung von PWM-Frequenzen
PWM_MOTOR_1.set_PWM_frequency(MOTOR_1, 10000)
PWM_MOTOR_2.set_PWM_frequency(MOTOR_2, 10000)
PWM_MOTOR_3.set_PWM_frequency(MOTOR_3, 10000)
PWM_MOTOR_4.set_PWM_frequency(MOTOR_4, 10000)

# Initialisierung von PWM-Duty-Cylces
PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, 0)
PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, 0)
PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, 0)
PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, 0)


# Server Starten
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is listening...")








# Werte des MPU auslesen
def mpu6050_werte():
    sensor = mpu6050(0x68)
    acceleration_data = sensor.get_accel_data()
    gyro_data = sensor.get_gyro_data()
    print("Acceleration Data")
    print(f"x: {acceleration_data['x']}")
    print(f"y: {acceleration_data['y']}")
    print(f"z: {acceleration_data['z']}")
    print("Gyro Data")
    print(f"x: {gyro_data['x']}")
    print(f"y: {gyro_data['y']}")
    print(f"z: {gyro_data['z']}")
    time.sleep(0.5)

# Speichern der Gyro-Daten in das gestreamte JSON-Dokument
def save_gyro_data():
    sensor = mpu6050(0x68)
    gyro_data = sensor.get_gyro_data()

    with open('gyro_data.json', 'w') as file:
        json.dump(gyro_data, file)
    
    gyro_data = {
        'x': gyro_data['x'],
        'y': gyro_data['y'],
        'z': gyro_data['z']
    }
    
save_gyro_data()


# Balancing-Funktion
def drohne_gerade_halten(motor_value1, motor_value2, motor_value3, motor_value4):
    sensor = mpu6050(0x68)
    gyro_data = sensor.get_gyro_data()
    print("Gyro Data")
    print(f"x: {gyro_data['x']}")
    print(f"y: {gyro_data['y']}")
    print(f"z: {gyro_data['z']}")
   


    #Ausbalancieren von Rechtsneigungen
    time.sleep(0.5)
    if gyro_data['x'] > 0:
        print("Drohne neigt sich nach rechts")
        PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2 + 5)
        PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3 + 5)

    #Ausbalancieren von Linksneigungen
    elif gyro_data['x'] < 0:
        print("Drohne neigt sich nach links")
        PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1 + 5) 
        PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4 + 5)

    # Drohne ist gerade, keine Nachjustierung nötig    
    else:
        print("Drohne ist gerade")
    time.sleep(0.5)

    # Ausbalancieren von Vorneneigungen
    if gyro_data['y'] > 0:
        print("Drohne neigt sich nach vorne")
        PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1 + 5)
        PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2 + 5)

    # Ausbalancieren von Hintenneigungen
    elif gyro_data['y'] < 0:
        print("Drohne neigt sich nach hinten")
        PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3 + 5)
        PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4 + 5)
        
    # Drohne ist gerade, keine Nachjustierung nötig     
    else:
        print("Drohne ist gerade")
    time.sleep(0.5)

    # Drohne rotiert nach rechts
    if gyro_data['z'] > 0:
        print("Drohne dreht sich nach rechts")
        
    # Drohne rotiert nach links
    elif gyro_data['z'] < 0:
        print("Drohne dreht sich nach links")

    # Drohne rotiert nicht
    else:
        print("Drohne dreht sich nicht")
    time.sleep(0.5)















while True:
    # Verbindung Herstellen
    client_socket, address = server_socket.accept()
    print(f"Connection from {address}")

    try:
        while True:
            # Empfangen von Daten und speichern in einer Variable
            received_data = client_socket.recv(1024).decode().strip()
            if not received_data:
                break
            
            values = received_data.split(',')
            
            # Aussortieren falscher Daten
            if len(values) != 4:
                print("Received invalid data format. Expected 4 values separated by comma.")
                continue

            else:
                motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)

                # Empfangene DutyCycle-Prozente werden an die Motoren weitergegeben
                PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1)
                PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2)
                PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3)
                PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4)


                # Balancing-Funktion wird ausgeführt
                drohne_gerade_halten(motor_value1, motor_value2, motor_value3, motor_value4)

                # Optionelle Ausgabe der enpfangenen Daten in der Konsole
                print("Received Motor Values (PWM %):")
                print("Motor 1:", motor_value1)
                print("Motor 2:", motor_value2)
                print("Motor 3:", motor_value3)
                print("Motor 4:", motor_value4)

                
            
    # Falsch Empfangene Daten -> Server schließen
    except Exception as e:
        print("Error receiving data:", e)
    
    client_socket.close()

# PWM anhalten und GPIO cleanup
    PWM_MOTOR_1.stop()
    PWM_MOTOR_2.stop()
    PWM_MOTOR_3.stop()
    PWM_MOTOR_4.stop()

    GPIO.stop()