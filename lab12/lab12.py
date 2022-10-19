from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import sys

class AlignDelegate(QtWidgets.QStyledItemDelegate):
    # Выравнивание значения ячейки по центру
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = QtCore.Qt.AlignCenter


class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решаем СЛУ")
        self.setFont(QtGui.QFont('Arial', 12))
        max_x = 500
        max_y = 300
        self.resize(max_x, max_y) 
        count = 5

        # Созданию меню и пунктов
        bar = QtWidgets.QMenuBar(self)
        task = QtWidgets.QAction("Задание", self)
        clear = QtWidgets.QAction("Очистить", self)
        result = QtWidgets.QAction("Результат", self)

        # Добавление к пунктам функций
        task.triggered.connect(self.task_action)
        clear.triggered.connect(self.clear_action)
        result.triggered.connect(self.result_action)

        # Добавление пунктов к меню
        bar.addAction(task)
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
        self.matrix.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.matrix.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Таблица для ввода вектора
        self.vector = QtWidgets.QTableWidget(count, 1)
        self.vector.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.vector.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # layout для таблицы матрицы и вектора
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(self.matrix)
        self.h_layout.addWidget(self.vector)

        # Таблица для вывода результата
        self.result = QtWidgets.QTableWidget(1, count)
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

        # Первоначальная настройка таблиц
        self.clear_action()

    def task_action(self):
        eq = [
            [0, 0, 12, -18, 5], 
            [-2, 4, 3, 5, 0], 
            [-1, 2, 3, 0, 1],
            [-4, 8, 12, -6, 13],
            [0, 0, 0, 0, 0]]
        vector = [-9, -7, -4, -1, 0]

        for i in range(self.matrix.columnCount()):
            for j in range(self.matrix.rowCount()):
                self.matrix.setItem(i, j, QtWidgets.QTableWidgetItem(str(eq[i][j])))
                self.vector.setItem(0, j, QtWidgets.QTableWidgetItem(str(vector[j])))

    def clear_action(self):
        delegate = AlignDelegate(self.matrix)
        header_matrix = ["x1", "x2", "x3", "x4", "x5"]
        header_vector = ["="]

        self.matrix.clear()
        self.matrix.setItemDelegate(delegate)
        self.matrix.setHorizontalHeaderLabels(header_matrix)
        self.set_zero(self.matrix)

        self.vector.clear()
        self.vector.setItemDelegate(delegate)
        self.vector.setHorizontalHeaderLabels(header_vector)
        self.set_zero(self.vector)

        self.result.clear()
        self.result.setItemDelegate(delegate)
        self.result.setHorizontalHeaderLabels(header_matrix)

    def result_action(self):
        eq = []
        vector = []
        # Добавляем значения с таблицы в списки
        try:
            for i in range(self.matrix.columnCount()):
                temp = []
                vector.append(int(self.vector.model().index(i, 0).data()))
                for j in range(self.matrix.rowCount()):
                    temp.append(int(self.matrix.model().index(i, j).data()))
                eq.append(temp)

            # Решаем СЛУ
            M2 = np.array(eq) # Матрица (левая часть системы)
            v2 = np.array(vector) # Вектор (правая часть системы)
            answer = np.linalg.lstsq(M2, v2)

            # Отображаем СЛУ
            for j in range(self.result.columnCount()):
                number = round(answer[0][j], 5)
                self.result.setItem(0, j, QtWidgets.QTableWidgetItem(str(number)))
        except:
            QtWidgets.QMessageBox.about(self, 
            "Критическая ошибка", 
            "Ошибка! В поле таблицы должно быть введено число")

    def set_zero(self, table = None):
        for i in range(table.columnCount()):
            for j in range(table.rowCount()):
                table.setItem(i, j, QtWidgets.QTableWidgetItem("0"))

def main():
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    window = Window()  # создаём объект класса ExampleApp
    window.show()  # показываем окно
    app.exec_()  # запускаем приложение

# Если файл запущен напрямую
if __name__ == '__main__':
    main()