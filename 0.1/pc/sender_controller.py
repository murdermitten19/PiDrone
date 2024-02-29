import tkinter as tk
import socket

# Drone server address and port (change this to match your Raspberry Pi's IP and port)
DRONE_SERVER_IP = '192.168.1.100'
DRONE_SERVER_PORT = 12345

# Create a socket connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Function to send drone commands
def send_command(command):
    try:
        sock.send(command.encode())
    except Exception as e:
        print("Error sending command:", e)

# Connect to the drone server and listen for user input
def connect_and_listen(ip_address):
    global DRONE_SERVER_IP
    DRONE_SERVER_IP = ip_address
    try:
        sock.connect((DRONE_SERVER_IP, DRONE_SERVER_PORT))
    except Exception as e:
        print("Error connecting to drone server:", e)
        return

    def key_press(event):
        key = event.keysym
        if key == 'w':
            send_command('forward')
        elif key == 'a':
            send_command('left')
        elif key == 's':
            send_command('back')
        elif key == 'd':
            send_command('right')
        elif key == 'Shift_L':
            send_command('up')
        elif key == 'Control_L':
            send_command('down')

    def key_release(event):
        send_command('stop')

    # Bind keyboard events
    root.bind('<KeyPress>', key_press)
    root.bind('<KeyRelease>', key_release)

    print("Connected to drone server.")

    # Destroy IP entry window and show main window
    ip_entry_window.destroy()
    show_main_window()

# Create main window with button to open IP choosing window
def show_main_window():
    global root
    root = tk.Tk()
    root.title("Drone Controller")

    open_ip_button = tk.Button(root, text="Choose IP", command=open_ip_entry_window)
    open_ip_button.pack()

    root.mainloop()

# Create IP choosing window
def open_ip_entry_window():
    global ip_entry_window
    ip_entry_window = tk.Toplevel(root)
    ip_entry_window.title("Enter Drone IP")

    label = tk.Label(ip_entry_window, text="Enter Drone IP:")
    label.pack()

    entry = tk.Entry(ip_entry_window)
    entry.pack()

    connect_button = tk.Button(ip_entry_window, text="Connect", command=lambda: connect_and_listen(entry.get()))
    connect_button.pack()

    # Hide the main window
    root.withdraw()

    # When IP window closes, show main window
    ip_entry_window.protocol("WM_DELETE_WINDOW", on_closing_ip_window)

def on_closing_ip_window():
    global root
    root.deiconify()  # Show the main window
    ip_entry_window.destroy()  # Destroy the IP window

# Start by showing the main window
show_main_window()

# Close the socket when the GUI closes
sock.close()
