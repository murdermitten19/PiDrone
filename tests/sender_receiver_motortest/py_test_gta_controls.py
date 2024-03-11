import tkinter as tk
import keyboard


HOVER_SPEED = 130

motor_speeds = [HOVER_SPEED, HOVER_SPEED, HOVER_SPEED, HOVER_SPEED]

LOWER = 127
HIGHER = 133



def fly_up():
    motor_speeds[0] =  HIGHER
    motor_speeds[1] =  HIGHER
    motor_speeds[2] =  HIGHER
    motor_speeds[3] =  HIGHER

def fly_down():
    motor_speeds[0] =  LOWER
    motor_speeds[1] =  LOWER
    motor_speeds[2] =  LOWER
    motor_speeds[3] =  LOWER

def rotate_left():
    motor_speeds[0] =  LOWER
    motor_speeds[1] =  HIGHER
    motor_speeds[2] =  LOWER
    motor_speeds[3] =  HIGHER

def rotate_right():
    motor_speeds[0] =  HIGHER
    motor_speeds[1] =  LOWER
    motor_speeds[2] =  HIGHER
    motor_speeds[3] =  LOWER

def tilt_forward():
    motor_speeds[0] =  LOWER
    motor_speeds[1] =  LOWER
    motor_speeds[2] =  HIGHER
    motor_speeds[3] =  HIGHER

def tilt_backward():
    motor_speeds[0] =  HIGHER
    motor_speeds[1] =  HIGHER
    motor_speeds[2] =  LOWER
    motor_speeds[3] =  LOWER

def tilt_left():
    motor_speeds[0] =  LOWER
    motor_speeds[1] =  HIGHER
    motor_speeds[2] =  HIGHER
    motor_speeds[3] =  LOWER

def tilt_right():
    motor_speeds[0] =  HIGHER
    motor_speeds[1] =  LOWER
    motor_speeds[2] =  LOWER
    motor_speeds[3] =  HIGHER

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

def on_key_release(event):
    event.char.lower() in ['a', 'b','c', 'd', '8', '5', '4', '6']
    reset_motor_speeds()
    print("1")

def reset_motor_speeds():
    global motor_speeds
    motor_speeds = [HOVER_SPEED, HOVER_SPEED, HOVER_SPEED, HOVER_SPEED]

def print_motor_speeds():
    print("Motor Speeds:", motor_speeds)
    root.after(100, print_motor_speeds)

def close_window():
    keyboard.unhook_all()
    root.destroy()




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
root.mainloop()