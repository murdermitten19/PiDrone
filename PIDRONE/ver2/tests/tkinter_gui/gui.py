import tkinter as tk

root = tk.Tk()

available_connections = ["192.168.0.100", "192.168.0.101"]



# set size of window
root.geometry("500x500")
root.option_add('*tearOff', False)
root.columnconfigure(0, weight=1)











# Function to switch screens
def switch_screen(screen):
    screen.tkraise()











# Create screens
screen1 = tk.Frame(root)
screen2 = tk.Frame(root)
screen3 = tk.Frame(root)

# Add screens to the root window
for screen in (screen1, screen2, screen3):
    screen.grid(row=0, column=0, sticky='nsew')



# Add text to screens
# Screen 1
text1 = tk.Label(screen1, text='Welcome to PiDrone!', font=('Arial', 24))
text1.pack(pady=50)

connect_to_ip_button = tk.Button(screen1, text='Connect to IP', command=lambda: switch_screen(screen2))
connect_to_ip_button.pack(pady=10)






# Screen 2


def connect_to_selected_ip():
    ip = selected_ip.get()
    # Add your code to connect to the selected IP here
    # For example, you can print the selected IP
    print(f"Connecting to IP: {ip}")

def select_ip(event):
    selected_ip.set(show_available_ips.get(show_available_ips.curselection()))







text2 = tk.Label(screen2, text='This is Screen 2', font=('Arial', 24))
text2.pack(pady=50)

selected_ip = tk.StringVar()

show_available_ips = tk.Listbox(screen2, listvariable=selected_ip)
show_available_ips.pack(pady=10)

for connection in available_connections:
    show_available_ips.insert(tk.END, connection)


connect_button = tk.Button(screen2, text='Connect', command=connect_to_selected_ip)
connect_button.pack(pady=10)

show_available_ips.bind('<<ListboxSelect>>', select_ip)





# Screen 3
text3 = tk.Label(screen3, text='This is Screen 3', font=('Arial', 24))
text3.pack(pady=50)














# Show initial screen
switch_screen(screen1)

root.mainloop()



