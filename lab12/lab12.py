from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решаем СЛУ")
        self.setFont(QtGui.QFont('Arial', 12))
        max_x = 500
        max_y = 300
        self.resize(max_x, max_y) 
        count = 5
        header_matrix = ["x1", "x2", "x3", "x4", "x5"]
        header_vector = ["="]

        # Созданию меню и пунктов
        bar = QtWidgets.QMenuBar(self)
        example1 = QtWidgets.QAction("Пример 1", self)
        example2 = QtWidgets.QAction("Пример 2", self)
        clear = QtWidgets.QAction("Очистить", self)
        result = QtWidgets.QAction("Результат", self)

        # Добавление к пунктам функций
        example1.triggered.connect(self.example1_action)
        example2.triggered.connect(self.example2_action)
        clear.triggered.connect(self.clear_action)
        result.triggered.connect(self.result_action)

        # Добавление пунктов к меню
        bar.addAction(example1)
        bar.addAction(example2)
        bar.addAction(clear)
        bar.addAction(result)

        # layout для меню
        self.menu_layout = QtWidgets.QVBoxLayout()
        self.menu_layout.addWidget(bar)

        # Таблица для ввода матрицы
        self.matrix = QtWidgets.QTableWidget(count, count)
        size_x = int(max_x - (max_x / count + 1))
        size_y = int(max_y - (max_y / count + 1))
        self.matrix.setMinimumSize(QtCore.QSize(size_x, size_y))
        self.matrix.setHorizontalHeaderLabels(header_matrix)
        self.matrix.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.matrix.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Таблица для ввода вектора
        self.vector = QtWidgets.QTableWidget(count, 1)
        self.vector.setHorizontalHeaderLabels(header_vector)
        self.vector.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.vector.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # layout для таблицы матрицы и вектора
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(self.matrix)
        self.h_layout.addWidget(self.vector)

        # Таблица для вывода результата
        self.result = QtWidgets.QTableWidget(1, count)
        self.result.setHorizontalHeaderLabels(header_matrix)
        self.result.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.result.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.result.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # layout для таблицы с результатом
        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.addWidget(self.result)

        # Отображение созданных layout
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.menu_layout)
        self.main_layout.addLayout(self.h_layout)
        self.main_layout.addLayout(self.v_layout)

    def example1_action(self):
        return

    def example2_action(self):
        return

    def clear_action(self):
        return

    def result_action(self):
        return

def main():
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    window = Window()  # создаём объект класса ExampleApp
    window.show()  # показываем окно
    app.exec_()  # запускаем приложение

# Если файл запущен напрямую
if __name__ == '__main__':
    main()