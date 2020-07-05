import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from index import Ui_Dialog
import pyautogui as auto
import keyboard as key

app = QtWidgets.QApplication(sys.argv)
    
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def get_click():
    start_k = ui.lineEdit.text()
    stop_k = ui.lineEdit_2.text()

    while True:
        if key.is_pressed(start_k):
            auto.tripleClick()

        if key.is_pressed(stop_k):
            break


ui.pushButton.clicked.connect(get_click)

sys.exit(app.exec_())