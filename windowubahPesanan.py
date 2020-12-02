# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowUbahPesanan.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import iopesanan
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 681, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 130, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.statuslaundry = QtWidgets.QComboBox(self.centralwidget)
        self.statuslaundry.setGeometry(QtCore.QRect(420, 200, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statuslaundry.setFont(font)
        self.statuslaundry.setObjectName("statuslaundry")
        self.statuslaundry.addItem("")
        self.statuslaundry.addItem("")
        self.statuslaundry.addItem("")
        self.statuslaundry.addItem("")
        self.statuslaundry.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 190, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(218, 250, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.statsusbayar = QtWidgets.QComboBox(self.centralwidget)
        self.statsusbayar.setGeometry(QtCore.QRect(420, 260, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statsusbayar.setFont(font)
        self.statsusbayar.setObjectName("statsusbayar")
        self.statsusbayar.addItem("")
        self.statsusbayar.addItem("")
        self.ubah = QtWidgets.QPushButton(self.centralwidget)
        self.ubah.setGeometry(QtCore.QRect(220, 330, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ubah.setFont(font)
        self.ubah.setObjectName("ubah")
        self.ubah.clicked.connect(lambda: iopesanan.ubahPesanan(self.inputorder.text(), self.statuslaundry.currentText(), self.statsusbayar.currentText()))
        self.inputorder = QtWidgets.QLineEdit(self.centralwidget)
        self.inputorder.setGeometry(QtCore.QRect(420, 140, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inputorder.setFont(font)
        self.inputorder.setObjectName("inputorder")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "                                   Ubah Pesanan"))
        self.label_2.setText(_translate("MainWindow", "ID Order"))
        self.statuslaundry.setItemText(0, _translate("MainWindow", "Dicuci"))
        self.statuslaundry.setItemText(1, _translate("MainWindow", "Dikeringkan"))
        self.statuslaundry.setItemText(2, _translate("MainWindow", "Disetrika"))
        self.statuslaundry.setItemText(3, _translate("MainWindow", "Siap diambil"))
        self.statuslaundry.setItemText(4, _translate("MainWindow", "Dalam Pengantaran"))
        self.label_3.setText(_translate("MainWindow", "Status Laundry"))
        self.label_4.setText(_translate("MainWindow", "Status Pembayaran"))
        self.statsusbayar.setItemText(0, _translate("MainWindow", "Belum lunas"))
        self.statsusbayar.setItemText(1, _translate("MainWindow", "Lunas"))
        self.ubah.setText(_translate("MainWindow", "Ubah"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
