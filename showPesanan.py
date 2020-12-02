# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showPesanan.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import iopesanan
from getDetailPesanan import getPesanan

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LaundryTracker")
        MainWindow.resize(604, 518)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 80, 271, 31))
        self.textEdit.setObjectName("textEdit")
        
        #Search Pesanan
        self.buttonCari = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCari.setGeometry(QtCore.QRect(440, 80, 51, 23))
        self.buttonCari.setObjectName("buttonCari")
        self.buttonCari.clicked.connect(self.searchPesanan)


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 130, 91, 21))
        self.label.setObjectName("label")
        self.labelOrderID = QtWidgets.QLabel(self.centralwidget)
        self.labelOrderID.setGeometry(QtCore.QRect(350, 130, 81, 21))
        self.labelOrderID.setObjectName("labelOrderID")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 160, 91, 21))
        self.label_3.setObjectName("label_3")
        self.labelCustID = QtWidgets.QLabel(self.centralwidget)
        self.labelCustID.setGeometry(QtCore.QRect(350, 160, 81, 21))
        self.labelCustID.setObjectName("labelCustID")

        #Label untuk display
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 190, 91, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 220, 91, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 250, 91, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(160, 280, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 310, 91, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(160, 340, 91, 21))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(160, 370, 121, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(160, 400, 131, 21))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(160, 430, 131, 21))
        self.label_13.setObjectName("label_13")

        #Label Hasil Pencarian
        self.labelBerat = QtWidgets.QLabel(self.centralwidget)
        self.labelBerat.setGeometry(QtCore.QRect(350, 190, 81, 21))
        self.labelBerat.setObjectName("labelBerat")
        self.labelJenisCucian = QtWidgets.QLabel(self.centralwidget)
        self.labelJenisCucian.setGeometry(QtCore.QRect(350, 220, 81, 21))
        self.labelJenisCucian.setObjectName("labelJenisCucian")
        self.labelStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(350, 250, 81, 21))
        self.labelStatus.setObjectName("labelStatus")
        self.labelHarga = QtWidgets.QLabel(self.centralwidget)
        self.labelHarga.setGeometry(QtCore.QRect(350, 280, 81, 21))
        self.labelHarga.setObjectName("labelHarga")
        self.labelStatusBayar = QtWidgets.QLabel(self.centralwidget)
        self.labelStatusBayar.setGeometry(QtCore.QRect(350, 310, 81, 21))
        self.labelStatusBayar.setObjectName("labelStatusBayar")
        self.labelJenisLayanan = QtWidgets.QLabel(self.centralwidget)
        self.labelJenisLayanan.setGeometry(QtCore.QRect(350, 340, 81, 21))
        self.labelJenisLayanan.setObjectName("labelJenisLayanan")
        self.labelDateAwal = QtWidgets.QLabel(self.centralwidget)
        self.labelDateAwal.setGeometry(QtCore.QRect(350, 370, 101, 21))
        self.labelDateAwal.setObjectName("labelDateAwal")
        self.labelDateFinish = QtWidgets.QLabel(self.centralwidget)
        self.labelDateFinish.setGeometry(QtCore.QRect(350, 400, 101, 21))
        self.labelDateFinish.setObjectName("labelDateFinish")
        self.labelPenyerahan = QtWidgets.QLabel(self.centralwidget)
        self.labelPenyerahan.setGeometry(QtCore.QRect(350, 430, 101, 21))
        self.labelPenyerahan.setObjectName("labelPenyerahan")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 81, 31))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 604, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #Connect button dengan label dan fungsi
    def searchPesanan(self):
            self.msg = QtWidgets.QMessageBox()
            

            if self.textEdit.toPlainText().isdigit():
                
                hasilGet = getPesanan(self.textEdit.toPlainText())
                
                self.labelBerat.setText(hasilGet[2])
                self.labelCustID.setText(hasilGet[1])
                self.labelDateAwal.setText(hasilGet[8])
                self.labelDateFinish.setText(hasilGet[9])
                self.labelHarga.setText(hasilGet[5])
                self.labelJenisCucian.setText(hasilGet[3])
                self.labelJenisLayanan.setText(hasilGet[7])
                self.labelOrderID.setText(hasilGet[0])
                self.labelPenyerahan.setText(hasilGet[10])
                self.labelStatus.setText(hasilGet[4])
                self.labelStatusBayar.setText(hasilGet[6])

                self.msg.exec_()
            else:
                self.msg.setText('ID harus berupa integer.')
                self.msg.exec_()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laundry Tracker"))
        self.buttonCari.setText(_translate("MainWindow", "Cari"))
        self.label.setText(_translate("MainWindow", "OrderID"))
        self.labelOrderID.setText(_translate("MainWindow", ""))
        self.label_3.setText(_translate("MainWindow", "CustomerID"))
        self.labelCustID.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Berat"))
        self.label_6.setText(_translate("MainWindow", "Jenis Cucian"))
        self.label_7.setText(_translate("MainWindow", "Status"))
        self.label_8.setText(_translate("MainWindow", "Harga"))
        self.label_9.setText(_translate("MainWindow", "Status Bayar"))
        self.label_10.setText(_translate("MainWindow", "Jenis Layanan"))
        self.label_11.setText(_translate("MainWindow", "Tanggal Masuk Pesanan"))
        self.label_12.setText(_translate("MainWindow", "Tanggal Pesanan Selesai"))
        self.label_13.setText(_translate("MainWindow", "Cara Penyerahan"))
        self.labelBerat.setText(_translate("MainWindow", ""))
        self.labelJenisCucian.setText(_translate("MainWindow", ""))
        self.labelStatus.setText(_translate("MainWindow", ""))
        self.labelHarga.setText(_translate("MainWindow", ""))
        self.labelStatusBayar.setText(_translate("MainWindow", ""))
        self.labelJenisLayanan.setText(_translate("MainWindow", ""))
        self.labelDateAwal.setText(_translate("MainWindow", ""))
        self.labelDateFinish.setText(_translate("MainWindow", ""))
        self.labelPenyerahan.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

