import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.uic import loadUi

tick = QtGui.QColor("green")


class TodoModel(QtCore.QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def data(self, index, role):
        # how to display the data
        if role == QtCore.Qt.DisplayRole:
            _, text = self.todos[index.row()]
            return text
        if role == QtCore.Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        loadUi("todomain.ui", self)
        self.model = TodoModel(todos=[(False, "my first todo")])
        self.todoView.setModel(self.model)
        self.btn_add.pressed.connect(self.add)
        self.btn_delete.pressed.connect(self.delete)
        self.btn_complete.pressed.connect(self.complete)

    def add(self):
        text = self.todoEdit.text()
        text = text.strip()

        if text:
            todo = (False, text)
            self.model.todos.append(todo)
            self.model.layoutChanged.emit()
            self.todoEdit.setText("")

    def complete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (not status, text)
            print(self.model.todos[row])
            self.model.dataChanged.emit(index, index)
        self.todoView.clearSelection()

    def delete(self):
        indexes = self.todoView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            del self.model.todos[row]
            self.model.layoutChanged.emit()
        self.todoView.clearSelection()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
