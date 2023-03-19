import sys
from ui_main import Ui_MainWindow
from PyQt5 import QtWidgets
from lec_dashboard import LecMainWindow
from dashboard import MainWindow
from db import createDatabase


class StartWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        createDatabase()

        self.btn_admin_page.clicked.connect(self.to_admin)
        self.btn_lec_page.clicked.connect(self.to_lec)

    def to_admin(self):
        admin_page = MainWindow(main=self) # we initialize the mainwindow
        admin_page.show()
        self.close()

    def to_lec(self):
        lec_page = LecMainWindow(main=self)
        lec_page.show()
        self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    app.exec()
