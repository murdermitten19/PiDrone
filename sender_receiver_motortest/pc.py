# import tkinter as tk
# from tkinter import ttk
# import socket
# import time

# def on_individual_slider_change1(value):
#     global motor_value1
#     motor_value1 = int(float(value))  # Convert float string to float, then to int
#     send_motor_values()

# def on_individual_slider_change2(value):
#     global motor_value2
#     motor_value2 = int(float(value))  # Convert float string to float, then to int
#     send_motor_values()

# def on_individual_slider_change3(value):
#     global motor_value3
#     motor_value3 = int(float(value))  # Convert float string to float, then to int
#     send_motor_values()

# def on_individual_slider_change4(value):
#     global motor_value4
#     motor_value4 = int(float(value))  # Convert float string to float, then to int
#     send_motor_values()

# def on_all_sliders_change(value):
#     global motor_value1, motor_value2, motor_value3, motor_value4
#     value = int(float(value))  # Convert float string to float, then to int
#     motor_value1 = value
#     motor_value2 = value
#     motor_value3 = value
#     motor_value4 = value
#     # Update all individual sliders when "All Motors" slider changes
#     slider1.set(value)
#     slider2.set(value)
#     slider3.set(value)
#     slider4.set(value)
#     # Delay to ensure smooth update
#     root.after(50, send_motor_values)

# def send_motor_values():
#     global motor_value1, motor_value2, motor_value3, motor_value4
#     message = f"{motor_value1},{motor_value2},{motor_value3},{motor_value4}"
#     try:
#         client_socket.sendall(message.encode())
#         print("Sent:", message)
#     except Exception as e:
#         print("Error sending data:", e)

# # Create main window
# root = tk.Tk()
# root.title("Motor Sliders")

# # Initial motor values
# motor_value1 = 0
# motor_value2 = 0
# motor_value3 = 0
# motor_value4 = 0

# # Create labels
# label1 = ttk.Label(root, text="Motor 1")
# label2 = ttk.Label(root, text="Motor 2")
# label3 = ttk.Label(root, text="Motor 3")
# label4 = ttk.Label(root, text="Motor 4")
# label5 = ttk.Label(root, text="All Motors")

# # Create individual sliders
# slider1 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change1, orient=tk.HORIZONTAL)
# slider2 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change2, orient=tk.HORIZONTAL)
# slider3 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change3, orient=tk.HORIZONTAL)
# slider4 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change4, orient=tk.HORIZONTAL)

# # Create "All Motors" slider
# all_sliders = ttk.Scale(root, from_=0, to=100, command=on_all_sliders_change, orient=tk.HORIZONTAL)

# # Pack labels and sliders into the window
# label1.grid(row=0, column=0, padx=10, pady=5)
# label2.grid(row=1, column=0, padx=10, pady=5)
# label3.grid(row=2, column=0, padx=10, pady=5)
# label4.grid(row=3, column=0, padx=10, pady=5)
# label5.grid(row=4, column=0, padx=10, pady=5)

# slider1.grid(row=0, column=1, padx=10, pady=5)
# slider2.grid(row=1, column=1, padx=10, pady=5)
# slider3.grid(row=2, column=1, padx=10, pady=5)
# slider4.grid(row=3, column=1, padx=10, pady=5)
# all_sliders.grid(row=4, column=1, padx=10, pady=5)

# # Create a socket object
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Server address
# SERVER_ADDRESS = '192.168.2.142'
# SERVER_PORT = 12345  # Make sure this matches the server's port

# try:
#     # Connect to the server
#     client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
# except Exception as e:
#     print("Error connecting to server:", e)

# # Run the tkinter event loop
# root.mainloop()

# # Close the client socket when the GUI closes
# client_socket.close()




import tkinter as tk
from tkinter import ttk
import socket
import time

def on_individual_slider_change1(value):
    global motor_value1
    motor_value1 = int(float(value))  # Convert float string to float, then to int
    send_motor_values()

def on_individual_slider_change2(value):
    global motor_value2
    motor_value2 = int(float(value))  # Convert float string to float, then to int
    send_motor_values()

def on_individual_slider_change3(value):
    global motor_value3
    motor_value3 = int(float(value))  # Convert float string to float, then to int
    send_motor_values()

def on_individual_slider_change4(value):
    global motor_value4
    motor_value4 = int(float(value))  # Convert float string to float, then to int
    send_motor_values()

def on_all_sliders_change(value):
    global motor_value1, motor_value2, motor_value3, motor_value4
    value = int(float(value))  # Convert float string to float, then to int
    motor_value1 = value
    motor_value2 = value
    motor_value3 = value
    motor_value4 = value
    # Update all individual sliders when "All Motors" slider changes
    slider1.set(value)
    slider2.set(value)
    slider3.set(value)
    slider4.set(value)
    # Add a slight delay before sending to reduce the number of events
    send_motor_values()

def send_motor_values():
    global motor_value1, motor_value2, motor_value3, motor_value4
    message = f"{motor_value1},{motor_value2},{motor_value3},{motor_value4}"
    try:
        client_socket.sendall(message.encode())
        print("Sent:", message)
        time.sleep(0.02)
    except Exception as e:
        print("Error sending data:", e)

# Create main window
root = tk.Tk()
root.title("Motor Sliders")

# Initial motor values
motor_value1 = 0
motor_value2 = 0
motor_value3 = 0
motor_value4 = 0

# Create labels
label1 = ttk.Label(root, text="Motor 1")
label2 = ttk.Label(root, text="Motor 2")
label3 = ttk.Label(root, text="Motor 3")
label4 = ttk.Label(root, text="Motor 4")
label5 = ttk.Label(root, text="All Motors")

# Create individual sliders
slider1 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change1, orient=tk.HORIZONTAL)
slider2 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change2, orient=tk.HORIZONTAL)
slider3 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change3, orient=tk.HORIZONTAL)
slider4 = ttk.Scale(root, from_=0, to=100, command=on_individual_slider_change4, orient=tk.HORIZONTAL)

# Create "All Motors" slider
all_sliders = ttk.Scale(root, from_=0, to=100, command=on_all_sliders_change, orient=tk.HORIZONTAL)

# Pack labels and sliders into the window
label1.grid(row=0, column=0, padx=10, pady=5)
label2.grid(row=1, column=0, padx=10, pady=5)
label3.grid(row=2, column=0, padx=10, pady=5)
label4.grid(row=3, column=0, padx=10, pady=5)
label5.grid(row=4, column=0, padx=10, pady=5)

slider1.grid(row=0, column=1, padx=10, pady=5)
slider2.grid(row=1, column=1, padx=10, pady=5)
slider3.grid(row=2, column=1, padx=10, pady=5)
slider4.grid(row=3, column=1, padx=10, pady=5)
all_sliders.grid(row=4, column=1, padx=10, pady=5)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server address
SERVER_ADDRESS = '192.168.2.142'
SERVER_PORT = 12345

try:
    # Connect to the server
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
    print("Connected to server")

    # Run the Tkinter event loop
    root.mainloop()

except Exception as e:
    print("Error:", e)

finally:
    # Close the socket
    client_socket.close()
