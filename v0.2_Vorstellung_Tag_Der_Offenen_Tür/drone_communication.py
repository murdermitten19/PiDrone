import socket

class DroneCommunication:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, message):
        
        self.socket.send(message)

    def receive(self):
        return self.socket.recvfrom(1024)