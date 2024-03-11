import socket
import pigpio as GPIO

# Definieren der Host- und Portvariablen
HOST = '0.0.0.0'
PORT = 12345

# Definieren der Motorvariablen
MOTOR_1 = 18
MOTOR_2 = 12
MOTOR_3 = 19
MOTOR_4 = 13

# Erstellen Sie PWM-Instanzen für jeden Motor
PWM_MOTOR_1 = GPIO.pi()
PWM_MOTOR_2 = GPIO.pi()
PWM_MOTOR_3 = GPIO.pi()
PWM_MOTOR_4 = GPIO.pi()

# Setzen der PWM-Frequenz für jeden Motor
PWM_MOTOR_1.set_PWM_frequency(MOTOR_1, 500)
PWM_MOTOR_2.set_PWM_frequency(MOTOR_2, 500)
PWM_MOTOR_3.set_PWM_frequency(MOTOR_3, 500)
PWM_MOTOR_4.set_PWM_frequency(MOTOR_4, 500)

# Setzen des PWM-Dutycycles für jeden Motor auf 0
PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, 0)
PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, 0)
PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, 0)
PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, 0)

# Erstellen des Server-Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server hört zu...")


# Main loop
while True:
    # Verbindung von einem Client akzeptieren
    client_socket, address = server_socket.accept()
    print(f"Verbindung von {address}")

    try:
        while True:
            received_data = client_socket.recv(1024).decode().strip()
            if not received_data:
                break
            
            # Teilen der empfangenen Daten in 4 Werte
            values = received_data.split(',')

            # Überprüfung empfangener Daten
            if len(values) != 4:
                print("Ungültiges Datenformat erhalten. Erwartet wurden 4 durch Komma getrennte Werte.")
                continue

            else:
                print(values)
                motor_value1, motor_value2, motor_value3, motor_value4 = map(int, values)

                # Setzen Sie den PWM-Tastverhältniszyklus für jeden Motor auf den empfangenen Wert
                PWM_MOTOR_1.set_PWM_dutycycle(MOTOR_1, motor_value1)
                PWM_MOTOR_2.set_PWM_dutycycle(MOTOR_2, motor_value2)
                PWM_MOTOR_3.set_PWM_dutycycle(MOTOR_3, motor_value3)
                PWM_MOTOR_4.set_PWM_dutycycle(MOTOR_4, motor_value4)

                print("Empfangene Motorwerte (PWM %):")
                print("Motor 1:", motor_value1)
                print("Motor 2:", motor_value2)
                print("Motor 3:", motor_value3)
                print("Motor 4:", motor_value4)

    # Fehlerbehandlung
    except Exception as e:
        print("Fehler beim Empfangen von Daten:", e)
 
    # Schließen der Verbindung zum Client
    client_socket.close()

# Stoppen Sie PWM und bereinigen Sie GPIO
    PWM_MOTOR_1.stop()
    PWM_MOTOR_2.stop()
    PWM_MOTOR_3.stop()
    PWM_MOTOR_4.stop()

    GPIO.stop()
