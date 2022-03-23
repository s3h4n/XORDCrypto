from .src import Handler
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def main() -> None:
    """
    main is the entry point for the program.
    """
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Handler()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
