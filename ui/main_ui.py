# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(763, 406)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 250, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.start_separation)
        self.textEdit_voice_name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_voice_name.setGeometry(QtCore.QRect(290, 150, 291, 31))
        self.textEdit_voice_name.setObjectName("textEdit")
        self.label_voice_name = QtWidgets.QLabel(self.centralwidget)
        self.label_voice_name.setGeometry(QtCore.QRect(150, 160, 131, 21))
        self.label_voice_name.setObjectName("label_voice_name")
        self.textEdit_music_name = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_music_name.setGeometry(QtCore.QRect(290, 190, 291, 31))
        self.textEdit_music_name.setObjectName("textEdit_voice_name")
        self.label_music_name = QtWidgets.QLabel(self.centralwidget)
        self.label_music_name.setGeometry(QtCore.QRect(150, 200, 131, 21))
        self.label_music_name.setObjectName("label_music_name")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(70, 20, 401, 51))
        self.label_title.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 330, 451, 31))
        self.label_4.setObjectName("label_4")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(290, 270, 281, 21))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        ##############
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(590, 10, 151, 131))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("./img/image.jpeg"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.label_path = QtWidgets.QLabel(self.centralwidget)
        self.label_path.setGeometry(QtCore.QRect(290, 100, 291, 31))
        self.label_path.setObjectName("label_path")
        self.label_path.hide()
        self.pushButton_select = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_select.setGeometry(QtCore.QRect(110, 100, 131, 27))
        self.pushButton_select.setObjectName("pushButton_select")
        self.pushButton_select.clicked.connect(self.select_file)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 24))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle(_translate("MainWindow", "The Knapsac problem"))
        self.pushButton.setText(_translate("MainWindow", "Start ==>"))
        self.label_voice_name.setText(_translate("MainWindow", "Voice name"))
        self.label_music_name.setText(_translate("MainWindow", "Music name"))
        self.label_title.setText(_translate("MainWindow",
                                            "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; font-style:italic;\">TP TSG :        </span><span style=\" font-family:\'Roboto Slab,ff-tisa-web-pro,Georgia,Arial,sans-serif\'; font-size:xx-large; font-weight:696; font-style:italic; color:#3465a4; background-color:#fcfcfc;\">       Vocal separation</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><a href=\"https://github.com/MahamdiAmine/MahamdiAmine.github.io/blob/master/LICENSE.md\"><span style=\" text-decoration: underline; color:#0000ff;\">Copyright © 2019 Mahamdi Mohammed and Boukabene Randa .</span></a></p><p><br/></p></body></html>"))
        self.pushButton_select.setText(_translate("MainWindow", "Your Music Input"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuShow_Statistics.setTitle(_translate("MainWindow", "Show Statistics"))

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "/home/mahamdi/development/VocalSeparation/inputs/",
                                                   "All Files (*);;Music Files (*.mp3)", options=options)
        if file_path:
            self.label_path.setText(file_path)
            self.label_path.show()

    def start_separation(self):
        voice_name = self.textEdit_voice_name.toPlainText()
        music_name = self.textEdit_music_name.toPlainText()
        if voice_name == "":
            voice_name = "voice.mp3"
            self.textEdit_voice_name.setText(voice_name)
        if music_name == "":
            music_name = "music.mp3"
            self.textEdit_music_name.setText(music_name)
