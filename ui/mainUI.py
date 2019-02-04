# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 190, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(240, 80, 291, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 131, 21))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(240, 120, 291, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 131, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 401, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 300, 451, 31))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(310, 200, 231, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        ##############
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(590, 10, 151, 131))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("./img/image.jpeg"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")

        ################"

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 24))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuShow_Statistics = QtWidgets.QMenu(self.menubar)
        self.menuShow_Statistics.setObjectName("menuShow_Statistics")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(QtGui.QIcon('./img/check_mark.png'))
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuShow_Statistics.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Knapsac problem"))
        self.pushButton.setText(_translate("MainWindow", "Start ==>"))
        self.label.setText(_translate("MainWindow", "Voice name"))
        self.label_2.setText(_translate("MainWindow", "Voice name"))

        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">TP TSG :     </span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:xx-large; font-weight:696; font-style:italic; color:#3465a4; background-color:#fcfcfc;\">Vocal separation</span><span style=\" font-size:16pt; font-weight:600; font-style:italic;\"/></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/MahamdiAmine/MahamdiAmine.github.io/blob/master/LICENSE.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Copyright © 2019 Mahamdi Mohammed and Boukabene Randa .</span></a></p><p><br/></p></body></html>"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuShow_Statistics.setTitle(_translate("MainWindow", "Show Statistics"))

