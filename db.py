from PyQt5 import QtSql


def createDatabase():
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("db.sqlite3")
    if not db.open():
        print("Database failed to open")
    else:
        print("Database is open")
