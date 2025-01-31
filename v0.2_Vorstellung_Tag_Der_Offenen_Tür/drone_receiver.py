import socket

HOST = '192.168.178.39'
PORT = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server hört zu...")


while True:
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
