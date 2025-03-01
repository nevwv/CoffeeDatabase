import sys
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
import sqlite3


class CoffeeDatabase(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Coffee Database')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах', 'Описание вкуса', 'Цена', 'Объем упаковки'])
        self.layout.addWidget(self.table)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()

        self.query = QSqlQuery(self.db)

        self.query.exec('SELECT * FROM coffee')
        while self.query.next():
            row = self.query.value(0)
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(self.query.value(0))))
            self.table.setItem(row, 1, QTableWidgetItem(self.query.value(1)))
            self.table.setItem(row, 2, QTableWidgetItem(self.query.value(2)))
            self.table.setItem(row, 3, QTableWidgetItem(self.query.value(3)))
            self.table.setItem(row, 4, QTableWidgetItem(self.query.value(4)))
            self.table.setItem(row, 5, QTableWidgetItem(str(self.query.value(5))))
            self.table.setItem(row, 6, QTableWidgetItem(str(self.query.value(6))))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeDatabase()
    ex.show()
    sys.exit(app.exec())
