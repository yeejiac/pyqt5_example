from test import *
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QFileDialog
import sys
import os

# text =  ⣿⣿⣿⣿⡿⠟⢋⣑⣒⡚⠿⢿⣿⣿⣿⣿⣿⣶⣭⡻⢿⣿⣿ 
#         ⣿⡟⣡⠖⣵⣿⣿⣿⣿⣿⣿⣷⡌⣿⣿⣿⢟⣩⣭⣭⣄⠻⣿ 
#         ⣿⣷⢉⣴⣶⣶⣶⣶⣶⣭⣝⠻⢡⣯⢻⡇⢸⠿⠿⠿⠿⣧⢹ 
#         ⣿⢇⣾⢟⠛⣿⣿⣿⡿⡛⠻⣿⢸⣿⡆⣿⣶⣾⣿⣿⣷⣶⡆ 
#         ⣿⢸⣿⣦⣴⣿⣿⣿⣿⣤⣶⣿⣷⣭⣾⣿⣿⣿⣿⣿⣿⣿⡇ 
#         ⣿⢸⣿⣿⣿⡛⠿⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⣛⣛⢣ 
#         ⣿⣧⡙⠿⠿⡿⡐⣿⣿⡿⠁⣠⠶⡌⣿⣿⣿⣿⢸⢸⠋⠙⡇ 
#         ⣿⣿⣧⠘⠦⠖⣰⣶⣶⣦⠄⢣⣥⠇⣶⣶⣦⣀⣈⠘⠷⠾⣣

def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QtGui.QStandardItemModel()
        self.ui.listView.setModel(self.model)
        self.ui.buttonBox.accepted.connect(self.clickYes)
        self.ui.pushButton.clicked.connect(self.getPath)
        self.ui.pushButton_2.clicked.connect(self.showMouse)

    def showMouse(self):
        self.model.clear()
        it = QtGui.QStandardItem("⣿⣿⣿⣿⡿⠟⢋⣑⣒⡚⠿⢿⣿⣿⣿⣿⣿⣶⣭⡻⢿⣿⣿\n" +  "⣿⡟⣡⠖⣵⣿⣿⣿⣿⣿⣿⣷⡌⣿⣿⣿⢟⣩⣭⣭⣄⠻⣿\n" + "⣿⣷⢉⣴⣶⣶⣶⣶⣶⣭⣝⠻⢡⣯⢻⡇⢸⠿⠿⠿⠿⣧⢹\n"+
            "⣿⢇⣾⢟⠛⣿⣿⣿⡿⡛⠻⣿⢸⣿⡆⣿⣶⣾⣿⣿⣷⣶⡆\n" + "⣿⢸⣿⣦⣴⣿⣿⣿⣿⣤⣶⣿⣷⣭⣾⣿⣿⣿⣿⣿⣿⣿⡇\n" + "⣿⢸⣿⣿⣿⡛⠿⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡛⣛⣛⢣\n" + "⣿⣧⡙⠿⠿⡿⡐⣿⣿⡿⠁⣠⠶⡌⣿⣿⣿⣿⢸⢸⠋⠙⡇\n"+
            "⣿⣿⣧⠘⠦⠖⣰⣶⣶⣦⠄⢣⣥⠇⣶⣶⣦⣀⣈⠘⠷⠾⣣")
        self.model.appendRow(it)

    def clickYes(self):
        text = self.ui.lineEdit.text()
        if text == "":
            it = QtGui.QStandardItem("請輸入指令(分隔符號+逗點+字串位置)")
            self.model.appendRow(it)
        else:
            f = open(str(self.dir_path[0]),"r", encoding = "Big5")
            w = open(str("test.txt"), "w")
            lines = f.readlines()
            for i in lines:
                i = insert_str(i, text.split(",")[0], int(text.split(",")[1]))
                w.writelines(i)
                print(i)

    def getPath(self):
        self.dir_path = QFileDialog.getOpenFileName(self,"Choose Directory","", "*.txt")
        it = QtGui.QStandardItem(self.dir_path[0])
        self.model.appendRow(it)
        



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())