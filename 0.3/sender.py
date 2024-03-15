# Importieren der benötigten Bibliotheken
import tkinter as tk
import keyboard
import socket
import time

IP_ADDRESS = '192.168.2.148'
PORT = 12345




root = tk.Tk()
root.title("Key Sender")



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, PORT))





def key_press(event):
    message = '{}+'.format(event.char)
    if message in ['w+', 'a+', 's+', 'd+', '8+', '4+', '5+', '6+']:
        s.sendall(message.encode())
    else:
        print("Invalid message")


def key_release(event):
    message = '{}-'.format(event.char)
    if message in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:
        s.sendall(message.encode())
    else:
        print("Invalid message")



root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)

root.mainloop()
