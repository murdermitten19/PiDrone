# Importieren der benötigten Bibliotheken
import tkinter as tk
import keyboard
import socket
import time


# Variablen für die Geschwindigkeit
HOVER_SPEED = 130
motor_value1 = 130
motor_value2 = 130
motor_value3 = 130
motor_value4 = 130

LOWER = 127
HIGHER = 133

# Netzwerkeinstellungen
IP_ADDRESS = '192.168.0.100'
PORT = 12345

# Funktionen zur Steuerung der Drohne
def fly_up():
    # Erhöht die Geschwindigkeit aller Motoren
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  HIGHER
    motor_value3 =  HIGHER
    motor_value4 =  HIGHER

def fly_down():
    # Verringert die Geschwindigkeit aller Motoren
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  LOWER
    motor_value3 =  LOWER
    motor_value4 =  LOWER

def rotate_left():
    # Lässt die Drohne nach links drehen
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  HIGHER
    motor_value3 =  LOWER
    motor_value4 =  HIGHER

def rotate_right():
    # Lässt die Drohne nach rechts drehen
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  LOWER
    motor_value3 =  HIGHER
    motor_value4 =  LOWER

def tilt_forward():
    # Lässt die Drohne nach vorne kippen
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  LOWER
    motor_value3 =  HIGHER
    motor_value4 =  HIGHER

def tilt_backward():
    # Lässt die Drohne nach hinten kippen
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  HIGHER
    motor_value3 =  LOWER
    motor_value4 =  LOWER

def tilt_left():
    # Lässt die Drohne nach links kippen
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  HIGHER
    motor_value3 =  HIGHER
    motor_value4 =  LOWER

def tilt_right():
    # Lässt die Drohne nach rechts kippen
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  LOWER
    motor_value3 =  LOWER
    motor_value4 =  HIGHER

def on_key_press(event):
    # Funktion, die aufgerufen wird, wenn eine Taste gedrückt wird
    if event.name == 'w':
        fly_up()
    elif event.name == 's':
        fly_down()
    elif event.name == 'a':
        rotate_left()
    elif event.name == 'd':
        rotate_right()
    elif event.name == '8':
        tilt_forward()
    elif event.name == '5':
        tilt_backward()
    elif event.name == '4':
        tilt_left()
    elif event.name == '6':
        tilt_right()

    send_motor_values()

def on_key_release(event):
    # Funktion, die aufgerufen wird, wenn eine Taste losgelassen wird
    event.char.lower() in ['a', 'b','c', 'd', '8', '5', '4', '6']
    reset_motor_speeds()
    send_motor_values()

def reset_motor_speeds():
    # Setzt die Geschwindigkeit aller Motoren zurück
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 = 130
    motor_value2 = 130
    motor_value3 = 130
    motor_value4 = 130

def print_motor_speeds():
    # Druckt die Geschwindigkeiten der Motoren
    print("Motor Speeds:", motor_value1, motor_value2, motor_value3, motor_value4)
    root.after(100, print_motor_speeds)

def close_window():
    # Schließt das Fenster und beendet das Programm
    keyboard.unhook_all()
    root.destroy()

def send_motor_values():
    # Sendet die aktuellen Geschwindigkeiten der Motoren an den Server
    global motor_value1, motor_value2, motor_value3, motor_value4
    message = f"{motor_value1},{motor_value2},{motor_value3},{motor_value4}"
    try:
        client_socket.sendall(message.encode())
        print("Sent:", message)
        time.sleep(0.02)
    except Exception as e:
        print("Error sending data:", e)

def starten():
    # Startet die Drohne
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 = 133
    motor_value2 = 133
    motor_value3 = 133
    motor_value4 = 133
    send_motor_values()
    time.sleep(3)
    reset_motor_speeds()

def landen():
    # Landet die Drohne
    global motor_value1, motor_value2, motor_value3, motor_value4
    while motor_value1 > 130:
        motor_value1 -= 1
        motor_value2 -= 1
        motor_value3 -= 1
        motor_value4 -= 1
        send_motor_values()
        time.sleep(1)

# Erstellen des GUI
root = tk.Tk()
root.title("Drone Control")

instructions_label = tk.Label(root, text="Use 'w', 'a', 's', 'd', '8', '4', '5', '6' keys to control the drone.")
instructions_label.pack()

start_button = tk.Button(root, text="Start", command=starten)
start_button.pack()

land_button = tk.Button(root, text="Land", command=landen)
land_button.pack()

reset_label = tk.Label(root, text="Press 'esc' to exit.")
reset_label.pack()

keyboard.on_press(on_key_press)

root.bind('<KeyRelease>', on_key_release)

print_motor_speeds()
root.bind('<Escape>', lambda e: close_window())

# Erstellen des Sockets
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Verbindung zum Server herstellen
    client_socket.connect((IP_ADDRESS, PORT))
    print("Connected to server")

    # Starten der GUI-Schleife
    root.mainloop()

except Exception as e:
    print("Error:", e)

finally:
    # Schließen des Sockets
    client_socket.close()
