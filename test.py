# Form implementation generated from reading ui file 'ACKK2.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1166, 679)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 130, 1111, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(10, 250, 171, 61))
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton.setGeometry(QtCore.QRect(480, 410, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.timeEdit_2 = QtWidgets.QTimeEdit(parent=self.frame)
        self.timeEdit_2.setGeometry(QtCore.QRect(10, 350, 171, 61))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalSlider = QtWidgets.QSlider(parent=self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(430, 360, 201, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(parent=self.frame)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(430, 320, 201, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_3 = QtWidgets.QSlider(parent=self.frame)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(430, 280, 201, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalSlider_4 = QtWidgets.QSlider(parent=self.frame)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(430, 240, 201, 22))
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.progressBar = QtWidgets.QProgressBar(parent=self.frame)
        self.progressBar.setGeometry(QtCore.QRect(920, 410, 181, 24))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(parent=self.frame)
        self.progressBar_2.setGeometry(QtCore.QRect(920, 360, 181, 24))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(10, 230, 141, 16))
        self.label.setMaximumSize(QtCore.QSize(141, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 330, 141, 16))
        self.label_2.setMaximumSize(QtCore.QSize(141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(920, 340, 49, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(920, 390, 49, 16))
        self.label_4.setObjectName("label_4")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(340, 0, 521, 161))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1166, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Simpan"))
        self.label.setText(_translate("MainWindow", "Input Waktu Buka"))
        self.label_2.setText(_translate("MainWindow", "Input Waktu Tutup"))
        self.label_3.setText(_translate("MainWindow", "Sensor 1"))
        self.label_4.setText(_translate("MainWindow", "Sensor 2"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:700;\">GORDEN OTOMATIS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700;\">Kelompok 2</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:26pt; font-weight:700;\">SISTEM KENDALI</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
