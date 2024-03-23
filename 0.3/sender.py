# Importieren der benötigten Bibliotheken
import tkinter as tk
import keyboard
import socket
import time

IP_ADDRESS = '192.168.0.100'
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

def check_no_keys_pressed():
    keys = ['w', 'a', 's', 'd', '8', '4', '5', '6']
    for key in keys:
        if keyboard.is_pressed(key):
            message = "none"
            s.sendall(message.encode())
    return True

root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)
root.bind("<Visibility>", check_no_keys_pressed)

root.mainloop()

