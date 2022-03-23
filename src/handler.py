from ..packages import XORDCrypto
from ..packages import FileHelper
from subprocess import call
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Handler(object):
    def __init__(self) -> None:
        self.xordc = XORDCrypto()
        self.file = FileHelper()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.load_key_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_key_btn.setGeometry(QtCore.QRect(10, 20, 150, 40))
        self.load_key_btn.setObjectName("load_key_btn")
        self.load_key_btn.clicked.connect(self.load_key_action)

        self.open_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_btn.setGeometry(QtCore.QRect(10, 70, 150, 40))
        self.open_file_btn.setObjectName("open_file_btn")
        self.open_file_btn.clicked.connect(self.open_file_action)

        self.convert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.convert_btn.setGeometry(QtCore.QRect(640, 500, 150, 40))
        self.convert_btn.setObjectName("convert_btn")
        self.convert_btn.clicked.connect(self.convert_file_action)

        self.save_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_file_btn.setGeometry(QtCore.QRect(480, 500, 150, 40))
        self.save_file_btn.setObjectName("save_file_btn")
        self.save_file_btn.clicked.connect(self.save_file_action)

        self.key_path_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.key_path_display.setGeometry(QtCore.QRect(170, 20, 620, 40))
        self.key_path_display.setObjectName("key_path_display")

        self.file_path_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.file_path_display.setGeometry(QtCore.QRect(170, 70, 620, 40))
        self.file_path_display.setObjectName("file_path_display")

        self.output_console = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_console.setGeometry(QtCore.QRect(10, 150, 780, 330))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.output_console.setFont(font)
        self.output_console.setObjectName("output_console")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 130, 780, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        MainWindow.setMenuBar(self.menubar)

        self.actionNew_Key = QtWidgets.QAction(MainWindow)
        self.actionNew_Key.setObjectName("actionNew_Key")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")

        self.menuFile.addAction(self.actionNew_Key)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.load_key_btn.setText(_translate("MainWindow", "Load Key"))
        self.open_file_btn.setText(_translate("MainWindow", "Open File"))
        self.convert_btn.setText(_translate("MainWindow", "Convert"))
        self.save_file_btn.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Key.setText(_translate("MainWindow", "New Key"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def load_key_action(self):
        pass

    def open_file_action(self):
        pass

    def save_file_action(self):
        pass

    def convert_file_action(self):
        pass
