import socket

# Definieren der Host- und Portvariablen
HOST = '0.0.0.0'
PORT = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server hört zu...")



while True:

    client_socket, address = server_socket.accept()
    print(f"Verbindung von {address}")

    while True:
        received_data = client_socket.recv(1024).decode().strip()
        
        if received_data in ['w+', 'a+', 's+', 'd+', '8+', '4+', '5+', '6+']:
            print("Empfangen: {"Key pressed", received_data}")

        elif received_data in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:
            print("Empfangen: {"Key released", received_data}")



