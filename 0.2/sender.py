import tkinter as tk
import keyboard
import socket
import time


HOVER_SPEED = 130

motor_value1 = 130
motor_value2 = 130
motor_value3 = 130
motor_value4 = 130

LOWER = 127
HIGHER = 133

IP_ADDRESS = '192.168.2.148'
PORT = 12345



def fly_up():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  HIGHER
    motor_value3 =  HIGHER
    motor_value4 =  HIGHER

def fly_down():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  LOWER
    motor_value3 =  LOWER
    motor_value4 =  LOWER

def rotate_left():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  HIGHER
    motor_value3 =  LOWER
    motor_value4 =  HIGHER

def rotate_right():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  LOWER
    motor_value3 =  HIGHER
    motor_value4 =  LOWER

def tilt_forward():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  LOWER
    motor_value3 =  HIGHER
    motor_value4 =  HIGHER

def tilt_backward():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  HIGHER
    motor_value3 =  LOWER
    motor_value4 =  LOWER

def tilt_left():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  LOWER
    motor_value2 =  HIGHER
    motor_value3 =  HIGHER
    motor_value4 =  LOWER

def tilt_right():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 =  HIGHER
    motor_value2 =  LOWER
    motor_value3 =  LOWER
    motor_value4 =  HIGHER

def on_key_press(event):
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
    event.char.lower() in ['a', 'b','c', 'd', '8', '5', '4', '6']
    reset_motor_speeds()
    send_motor_values()

def reset_motor_speeds():
    global motor_value1, motor_value2, motor_value3, motor_value4
    motor_value1 = 130
    motor_value2 = 130
    motor_value3 = 130
    motor_value4 = 130

def print_motor_speeds():
    print("Motor Speeds:", motor_value1, motor_value2, motor_value3, motor_value4)
    root.after(100, print_motor_speeds)

def close_window():
    keyboard.unhook_all()
    root.destroy()

def send_motor_values():
    global motor_value1, motor_value2, motor_value3, motor_value4
    message = f"{motor_value1},{motor_value2},{motor_value3},{motor_value4}"
    try:
        client_socket.sendall(message.encode())
        print("Sent:", message)
        time.sleep(0.02)
    except Exception as e:
        print("Error sending data:", e)




root = tk.Tk()
root.title("Drone Control")

instructions_label = tk.Label(root, text="Use 'w', 'a', 's', 'd', '8', '4', '5', '6' keys to control the drone.")
instructions_label.pack()

reset_label = tk.Label(root, text="Press 'esc' to exit.")
reset_label.pack()

keyboard.on_press(on_key_press)

root.bind('<KeyRelease>', on_key_release)

print_motor_speeds()
root.bind('<Escape>', lambda e: close_window())


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
    
    client_socket.connect((IP_ADDRESS, PORT))
    print("Connected to server")

    
    root.mainloop()

except Exception as e:
    print("Error:", e)

finally:
    
    client_socket.close()

