import sys
from main_menu import *

  

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainMenu = MainWindow()
    
    MainMenu.show()
    sys.exit(app.exec_())

