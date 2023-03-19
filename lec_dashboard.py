import sys
from PyQt5 import QtCore, QtWidgets, QtSql
from PyQt5 import QtBluetooth as QtBt
from ui_lec_dashboard import Ui_MainWindow
from db import createDatabase


class CourseModel(QtCore.QAbstractListModel):
    def __init__(self, courses=[]) -> None:
        super().__init__()
        self.courses = courses

    def data(self, index, role: int):
        if role == QtCore.Qt.DisplayRole:
            _, name = self.courses[index.row()]
            return name

    def rowCount(self, index) -> int:
        return len(self.courses)


class DeviceModel(QtCore.QAbstractListModel):
    def __init__(self, devices=[]) -> None:
        super().__init__()
        self.devices = devices

    def data(self, index, role: int):
        if role == QtCore.Qt.DisplayRole:
            name, _ = self.devices[index.row()]
            return name

    def rowCount(self, index) -> int:
        return len(self.devices)


class LecMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, lecturer_id=None, main=None) -> None:
        super().__init__()
        self.main = main
        # createDatabase()
        self.setupUi(self)
        # initialize all functions and variable
        self.query = QtSql.QSqlQuery()
        self.recordmodel = QtSql.QSqlQueryModel()
        self.attendance_table.setModel(self.recordmodel)
        self.pages.setCurrentIndex(0)

        self.model = self.get_related_course()
        self.course_comboBox.setModel(self.model)
        self.course_code_comboBox.setModel(self.model)
        self.device_model = DeviceModel()
        self.blt_device_list.setModel(self.device_model)

        self.timeEdit.setTime(QtCore.QTime.currentTime())
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.course_dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.btn_attendance_record.pressed.connect(
            lambda: self.change_page("attendance_record")
        )
        self.btn_take_attendance.pressed.connect(
            lambda: self.change_page("take_attendance")
        )
        self.btn_take_attendance_2.pressed.connect(self._take_attendance)

        self.btn_scan_btl.clicked.connect(self.scan_btl)
        self.get_attendance.clicked.connect(self._get_attendance)
        self.btn_back.pressed.connect(self.back)

        # initialized bluetooth device
        self.agent = QtBt.QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.discovered)
        self.agent.finished.connect(self.finished)
        self.agent.error.connect(self.blt_error)
        # self.show()

    def _take_attendance(self):
        course_index = self.model.courses[self.course_comboBox.currentIndex()][0]
        class_time = self.timeEdit.time().toString()
        class_date = self.dateEdit.date().toString(QtCore.Qt.ISODate)
        print(course_index, class_time, class_date, sep="  ")
        if self.query.exec(
            f"""INSERT INTO record (course, date, time) VALUES ('{course_index}', '{class_date}', '{class_time}')"""
        ):
            if record_id := self.query.lastInsertId():
                for device in self.device_model.devices:
                    print(device, record_id)
                    if self.query.exec(
                        f"SELECT id FROM student WHERE bluetooth_id='{device[1]}'"
                    ):
                        if self.query.first():
                            self.query.exec(
                                f"""INSERT INTO student_record (record_id, student_id) VALUES ('{record_id}', '{self.query.value("id")}')"""
                            )
                QtWidgets.QMessageBox.information(self, "Success", "Attendance taken")
            #     # print(self.query.value(0))
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Error taking attendance")

    def _get_attendance(self):
        query = QtSql.QSqlQuery()
        course = self.model.courses[self.course_code_comboBox.currentIndex()][0]
        date = self.course_dateTimeEdit.date().toString(QtCore.Qt.ISODate)
        time = self.course_dateTimeEdit.time().toString()
        if query.exec(
            f"""
            SELECT student.matric,
       student.first_name, student.second_name
  FROM student_record
       INNER JOIN
       student ON student_record.student_id = student.id
       INNER JOIN
       record ON student_record.record_id = record.id
  WHERE record.course = {course} and record.date = '{date}' and record.time = '{time}'
            """
        ):

            pass
        else:
            print(query.lastError().text())
        self.recordmodel.setQuery(query)

    def change_page(self, page):
        if page == "attendance_record":
            self.pages.setCurrentWidget(self.attendance_record_page)
        elif page == "take_attendance":
            self.pages.setCurrentWidget(self.take_attendance_page)

    def back(self):
        start = self.main.show()
        self.close()

    def get_related_course(self):
        course_list = list(tuple())
        self.query.exec("SELECT id, course_code FROM course")
        while self.query.next():
            course_list.append(
                (self.query.value("id"), self.query.value("course_code"))
            )
        return CourseModel(course_list)

    def scan_btl(self):
        self.device_model.devices = []
        self.device_model.layoutChanged.emit()
        self.agent.start()
        self.btn_scan_btl.setDisabled(True)

    def finished(self):
        self.btn_scan_btl.setDisabled(False)
        QtWidgets.QMessageBox.information(self, "Success", "Scanning fininished")
        # print(self.agent.isActive(), self.agent.discoveredDevices())

    def discovered(self, info):
        device = (info.name(), info.address().toString())
        self.device_model.devices.append(device)
        self.device_model.layoutChanged.emit()

    def blt_error(self):
        self.btn_scan_btl.setDisabled(False)
        print("Error occurs")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LecMainWindow()
    app.exec()
