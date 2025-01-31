from PyQt5 import QtWidgets, uic
from drone_communication import *

class DroneController(QtWidgets.QDialog):
    def __init__(self, main_menu, ip, port):
        super(DroneController, self).__init__()
        uic.loadUi('motor_controller.ui', self)
        self.main_menu = main_menu
        self.ip = ip
        self.port = port
        self.drone_communication = DroneCommunication()

        self.pb_return_to_mm.clicked.connect(self.return_to_mm)
        self.sl_m1.valueChanged.connect(self.sl_value_changed)
        self.sl_m2.valueChanged.connect(self.sl_value_changed)
        self.sl_m3.valueChanged.connect(self.sl_value_changed)
        self.sl_m4.valueChanged.connect(self.sl_value_changed)

    def return_to_mm(self):
        self.main_menu.show_again()
        self.close()
        
    def connect_to_drone(self):
        print("1")
        ip = "192.168.178.39"
        print("2")
        port = 12345
        print("3")
        self.drone_communication.socket.connect((ip, port))
        print("4")

    def send_command(self, message):
        
        message_enc = message.encode()
        self.drone_communication.send(message_enc)

    def map_slider_value(self, value):
        return int(120 + (value / 99) * (255 - 120))

    def sl_value_changed(self):
        v1 = self.map_slider_value(self.sl_m1.value())
        v2 = self.map_slider_value(self.sl_m2.value())
        v3 = self.map_slider_value(self.sl_m3.value())
        v4 = self.map_slider_value(self.sl_m4.value())
        print(v1, v2, v3, v4)
        message = f"{v1},{v2},{v3},{v4}"
        self.send_command(message)


