from PyQt5 import QtWidgets, uic
import sys
from drone_controller import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_menu.ui', self)


        self.btn_conntect.clicked.connect(self.connect_to_ip)
        self.btn_close.clicked.connect(self.close)

        self.DroneControllingDialog = None


    def connect_to_ip(self):
        ip_userinput = self.le_ip_ui.text()
        port_userinput = self.le_port_ui.text()
        
        
        self.DroneControllingDialog = DroneController(self, ip_userinput, port_userinput)
        self.hide()
        print(ip_userinput, port_userinput)
        self.DroneControllingDialog.connect_to_drone()
        
        IPandPORT = f"{ip_userinput}:{port_userinput}"
        self.DroneControllingDialog.lbl_curr_ip_port.setText(IPandPORT)
        self.DroneControllingDialog.show()
        self.DroneControllingDialog.exec_()
        
        

    def show_again(self):
        self.showNormal()