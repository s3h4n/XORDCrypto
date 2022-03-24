from PyQt5 import QtCore, QtGui, QtWidgets
from ..packages import XORDCrypto
from ..packages import FileHelper
from . import constants
from datetime import datetime
import sys


class Handler(object):
    def __init__(self) -> None:
        self.xordc = XORDCrypto()
        self.file = FileHelper()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)

        self.MainWindow = MainWindow
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(
            QtGui.QPixmap("XORDCrypto/resources/KeyLow_Safety.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        MainWindow.setWindowIcon(self.icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Following button will open up a file browser and let user to choose a key file.
        self.load_key_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_key_btn.setGeometry(QtCore.QRect(10, 20, 150, 40))
        self.load_key_btn.setObjectName("load_key_btn")
        self.load_key_btn.clicked.connect(self.load_key_action)

        # Following button will open up a file browser and let user to select a file to encryption/decryption.
        self.open_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.open_file_btn.setGeometry(QtCore.QRect(10, 70, 150, 40))
        self.open_file_btn.setObjectName("open_file_btn")
        self.open_file_btn.setEnabled(False)
        self.open_file_btn.clicked.connect(self.open_file_action)

        # following button will encrypt/decrypt the given file.
        self.convert_btn = QtWidgets.QPushButton(self.centralwidget)
        self.convert_btn.setGeometry(QtCore.QRect(640, 500, 150, 40))
        self.convert_btn.setObjectName("convert_btn")
        self.convert_btn.setCheckable(True)
        self.convert_btn.setChecked(False)
        self.convert_btn.setEnabled(False)
        self.convert_btn.clicked.connect(self.convert_file_action)

        # Following button will open up a file browser and let user to save ecnrypted/decrypted file.
        self.save_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_file_btn.setGeometry(QtCore.QRect(480, 500, 150, 40))
        self.save_file_btn.setObjectName("save_file_btn")
        self.save_file_btn.setEnabled(False)
        self.save_file_btn.clicked.connect(self.save_file_action)

        # This will show the path of the key.
        self.key_path_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.key_path_display.setGeometry(QtCore.QRect(170, 20, 620, 40))
        self.key_path_display.setObjectName("key_path_display")

        # This will show the path of the file.
        self.file_path_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.file_path_display.setGeometry(QtCore.QRect(170, 70, 620, 40))
        self.file_path_display.setObjectName("file_path_display")

        # This will show the outputs of tasks.
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
        self.actionNew_Key.triggered.connect(self.new_key_action)

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.about_dialog)

        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.quit_action)

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
        MainWindow.setWindowTitle(_translate("MainWindow", "XORDCrypto"))
        self.load_key_btn.setText(_translate("MainWindow", "Load Key"))
        self.open_file_btn.setText(_translate("MainWindow", "Open File"))
        self.convert_btn.setText(_translate("MainWindow", "Convert"))
        self.save_file_btn.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Key.setText(_translate("MainWindow", "New Key"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    def create_log(self, text: str) -> None:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.output_console.append(f"[{current_time}] ➡️ {text}")

    def new_key_action(self) -> None:
        new_key = self.xordc.generate_key(32)
        new_key_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.MainWindow, "Save Key", "", "Key Files (*.key)"
        )
        if new_key_path:
            self.file.write_file(new_key_path, new_key)
            self.create_log(f"Key saved in {new_key_path}")
        else:
            self.create_log(f"Adding new key has aborted.")

    def load_key_action(self) -> None:
        self.key_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "Open a Key", "", "Key Files (*.key)"
        )
        if self.key_path:
            self.open_file_btn.setEnabled(True)
            self.key_path_display.setText(self.key_path)
            self.key = self.file.read_file(self.key_path)
            self.create_log("Key file has successfully loaded.")
        else:
            self.open_file_btn.setEnabled(False)
            self.convert_btn.setEnabled(False)
            self.save_file_btn.setEnabled(False)
            self.key_path_display.setText("")
            self.file_path_display.setText("")
            self.create_log(f"Loading key file has failed.")

    def open_file_action(self) -> None:
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "Open a File", "", "All Files (*)"
        )
        if self.file_path:
            self.convert_btn.setEnabled(True)
            self.file_path_display.setText(self.file_path)
            self.data = self.file.read_file(self.file_path)
            self.create_log("File has successfully loaded.")
        else:
            self.convert_btn.setEnabled(False)
            self.save_file_btn.setEnabled(False)
            self.file_path_display.setText("")
            self.create_log(f"Loading File has failed.")

    def convert_file_action(self) -> None:
        if self.data and self.key:
            self.output = self.xordc.convert(self.key, self.data)
            if self.convert_btn.isChecked():
                self.create_log("File has converted.")
                self.save_file_btn.setEnabled(True)
            else:
                self.create_log("File has reversed to original state.")
                self.save_file_btn.setEnabled(False)

    def save_file_action(self) -> None:
        output_path, _ = QtWidgets.QFileDialog.getSaveFileName(
            self.MainWindow, "Save Output", "", "All Files (*)"
        )
        if self.output and output_path:
            self.file.write_file(output_path, self.output)
            self.create_log(f"Output saved in {output_path}")
        else:
            self.create_log(f"Saving output has aborted.")

    def quit_action(self) -> None:
        sys.exit()

    def about_dialog(self):
        about_dialog = QtWidgets.QMessageBox()
        about_dialog.setWindowTitle("About")

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(
            QtGui.QPixmap("XORDCrypto/resources/KeyLow_Safety.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        about_dialog.setIconPixmap(self.icon.pixmap(QtCore.QSize(180, 180)))

        about_dialog.setText(
            "\n<h3 style='font-family:Ubuntu,sans-serif;'>XORDCrypto</h3>"
        )
        about_dialog.setInformativeText(constants.ABOUT)

        about_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        about_dialog.setDefaultButton(QtWidgets.QMessageBox.Ok)

        about_dialog.exec_()
