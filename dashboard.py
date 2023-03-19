import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5 import QtBluetooth as QtBt
from PyQt5.QtSql import QSqlQuery
from ui_dashboard import Ui_MainWindow


class LecturerModel(QtCore.QAbstractListModel):
    def __init__(self, items=[]) -> None:
        super().__init__()
        self.items = items

    def data(self, index, role: int):
        # how to display the data
        if role == QtCore.Qt.DisplayRole:
            # we unpack the tuple
            _, text = self.items[index.row()]
            return text

    def rowCount(self, index) -> int:
        return len(self.items)


class DeviceModel(QtCore.QAbstractListModel):
    """The model for bluetooth devices"""
    def __init__(self, devices=[]) -> None:
        super().__init__()
        self.devices = devices

    def data(self, index, role: int):
        if role == QtCore.Qt.DisplayRole:
            name, _ = self.devices[index.row()]
            return name

    def rowCount(self, index) -> int:
        return len(self.devices)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, main=None):
        super().__init__()
        self.main = main
        self.setupUi(self)
        self.query = QSqlQuery()
        self.pages.setCurrentIndex(0)

        self.lecturer_model = self._set_lecturer_model()
        self.course_lec_combox.setModel(self.lecturer_model)

        self.device_model = DeviceModel(devices=[])
        self.blt_device_list.setModel(self.device_model)

        self.btn_create_lecturer.pressed.connect(
            lambda: self.changePage(self.create_lecturer_page)
        )
        self.btn_create_course.pressed.connect(
            lambda: self.changePage(self.create_course_page)
        )
        self.btn_create_student.pressed.connect(
            lambda: self.changePage(self.create_student_page)
        )

        # get lecturers id for assigning course to lecture

        # submit button func assign
        self.btn_add_lecturer.pressed.connect(self._create_lecturer)
        self.btn_add_student.pressed.connect(self._create_student)
        self.btn_add_course.pressed.connect(self._create_course)
        self.btn_back.pressed.connect(self.back)

        # initialize bluetooth device
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.discovered)
        self.agent.finished.connect(self.finished)
        self.agent.error.connect(self.blt_error)

        self.btn_scan_btl.pressed.connect(self._scan_blt_device)
        # self.show()

    def changePage(self, page):
        # change pages
        self.initialize()
        self.pages.setCurrentWidget(page)

    def back(self):
        start = self.main.show()
        self.close()

    def initialize(self):
        self.lecturer_model = self._set_lecturer_model()
        self.course_lec_combox.setModel(self.lecturer_model)

    def _create_lecturer(self):
        fname = self.lec_fname_edit.text()
        sname = self.lec_sname_edit.text()
        department = self.lec_depart_edit.text()
        password = self.lec_password.text()

        if (fname != "") and (sname != "") and (password != ""):
            # call the query here
            print("Here")
            if self.query.exec(
                f"""INSERT INTO lecturer (first_name, second_name, password) VALUES ('{fname}','{sname}','{password}')"""
            ):
                # call the success here
                QtWidgets.QMessageBox.information(
                    self, "Success", "Successfully created lecturer"
                )
            else:
                # call the error message
                QtWidgets.QMessageBox.critical(
                    self, "Error", "Failed to create lecturer"
                )
            pass
        else:
            self.lecturer_err.setText("all fields should not be empty")

    def _create_student(self):
        indexes = self.blt_device_list.selectedIndexes()
        matric = self.stu_matric_edit.text()
        fname = self.stu_fname_edit.text()
        sname = self.stu_sname_edit.text()
        department = self.stu_depart_edit.text()
        if len(indexes) != 0:
            index = indexes[0]
            row = index.row()
            _, blt_id = self.device_model.devices[row]
        if (
            (matric != "")
            and (fname != "")
            and (sname != "")
            and (department != "")
            and (blt_id != "")
        ):
            if True:
                result = self.query.exec(
                    f"""INSERT INTO student (first_name, second_name, department, bluetooth_id, matric) VALUES ('{fname}', '{sname}', '{department}', '{blt_id}', '{matric}')"""
                )
                print(matric, fname, sname, department, blt_id)
                print(result)
                if result:
                    QtWidgets.QMessageBox.information(
                        self, "Success", "Successfully create student"
                    )
                else:
                    print(self.query.lastError().text())
                    QtWidgets.QMessageBox.critical(
                        self, "Error", "Failed to create student"
                    )
            else:
                print("blt is not a string")
        else:
            self.student_err.setText("all fields should not be empty")

    def _create_course(self):
        course_code = self.course_code_edit.text()
        course_title = self.course_title_edit.text()
        course_lec_index = self.course_lec_combox.currentIndex()
        if (course_title != "") and (course_code != "") and (course_lec_index != ""):
            if course_lec_index != None:
                course_lec_id, _ = self.lecturer_model.items[course_lec_index]
            if self.query.exec(
                f"""INSERT INTO course (course_code, course_title, lecturer) VALUES ('{course_code}', '{course_title}', '{course_lec_id}')"""
            ):
                QtWidgets.QMessageBox.information(
                    self, "Success", "Successfully create course"
                )
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Failed to create course")
        else:
            self.course_err.setText("All fields should not be empty")

    def _scan_blt_device(self):
        """Start scanning the bluetooth"""
        self.device_model.devices = []
        self.device_model.layoutChanged.emit()
        self.agent.start()
        self.btn_scan_btl.setDisabled(True)

    def finished(self):
        """After bluetooth finished scanning"""
        self.btn_scan_btl.setDisabled(False)
        QtWidgets.QMessageBox.information(self, "Success", "Scanning fininished")

    def discovered(self, info):
        """store it to a list"""
        device = (info.name(), info.address().toString())
        self.device_model.devices.append(device)
        self.device_model.layoutChanged.emit()

    def blt_error(self):
        self.btn_scan_btl.setDisabled(False)
        print("Error occurs")

    def _set_lecturer_model(self):
        lecturer_list = []
        self.query.exec("SELECT id, first_name, second_name FROM lecturer")
        while self.query.next():
            lecturer_list.append(
                (
                    self.query.value("id"),
                    f"{self.query.value('first_name')} {self.query.value('second_name')}",
                )
            )
        return LecturerModel(lecturer_list)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec()
