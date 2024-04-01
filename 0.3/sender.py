# Importieren der benötigten Bibliotheken
import tkinter as tk
import keyboard
import socket
import time

IP_ADDRESS = '192.168.0.100'
PORT = 12345




root = tk.Tk()
root.title("Key Sender")

# root.geometry("750x250")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, PORT))

Keypress = False


def key_press(event):

    global Keypress
    message = '{}+'.format(event.char)
    if message in ['w+', 'a+', 's+', 'd+', '8+', '4+', '5+', '6+']:
        s.sendall(message.encode())
        Keypress = True
    else:
        print("Invalid message")


def key_release(event):

    global Keypress
    message = '{}-'.format(event.char)
    if message in ['w-', 'a-', 's-', 'd-', '8-', '4-', '5-', '6-']:
        s.sendall(message.encode())
        Keypress = False
    else:
        print("Invalid message")

def check_no_keys_pressed():
    message = "w-"
    if Keypress == False:
        s.sendall(message.encode())
    else:
        p = 1   
    root.after(100, check_no_keys_pressed)

def arm_motors():
    message = "armmotors"
    s.sendall(message.encode())

def stop_motors():
    message = "stopmotors"
    s.sendall(message.encode())

def start_motors():
    message = "startmotors"
    s.sendall(message.encode())

def increase_speed():
    message = "increasespeed"
    s.sendall(message.encode())



root.bind("<KeyPress>", key_press)
root.bind("<KeyRelease>", key_release)
root.bind("Button", arm_motors)

arm_motors_button = tk.Button(root, text="Arm Motors", command=arm_motors)
stop_motors_button = tk.Button(root, text="Stop Motors", command=stop_motors)
start_motors_button = tk.Button(root, text="Start Motors/Allow Control", command=start_motors)
increase_speed_button = tk.Button(root, text="Increase Speed", command=increase_speed)


label_for_control = tk.Label(root, text="Drücken Sie die Pfeiltasten, um die Drohne zu steuern.")


arm_motors_button.pack()
start_motors_button.pack()
stop_motors_button.pack()
increase_speed_button.pack()
label_for_control.pack()


check_no_keys_pressed()
root.mainloop()

