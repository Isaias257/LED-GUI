from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys
from LED_RGB_GUI import Ui_LED_RBG_GUI

#Arduino needs to be connceted in order for the script to run successfully
import serial
Arduino = serial.Serial(port='COM3',baudrate=9600,timeout=1)
RGB = ['R0','G0','B0']

class MainWindow:
    def __init__(self):
        self.main_win = QWidget()
        self.ui = Ui_LED_RBG_GUI()
        self.ui.setupUi(self.main_win)
        self.ui.Red_value.valueChanged.connect(self.red_number_changed)
        self.ui.Green_value.valueChanged.connect(self.green_number_changed)
        self.ui.Blue_value.valueChanged.connect(self.blue_number_changed)
        self.ui.pushButton.clicked.connect(self.clickedpushbutton)

    def red_number_changed(self):
        Red_value = str(self.ui.Red_value.value())
        RGB[0] = 'R' + Red_value

    def green_number_changed(self):
        Green_value = str(self.ui.Green_value.value())
        RGB[1] = 'G' + Green_value

    def blue_number_changed(self):
        Blue_value = str(self.ui.Blue_value.value())
        RGB[2] = 'B' + Blue_value

    def clickedpushbutton(self):
        send_RBG = ''.join(RGB).encode('utf-8')
        Arduino.write(send_RBG)
        print(send_RBG)

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
