from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисуем линии")
        self.setFont(QtGui.QFont('Arial', 12))
        self.resize(500, 300) 

        # Горизонтальный layout
        self.label = QtWidgets.QLabel("Введите число")
        self.input = QtWidgets.QLineEdit()
        self.button = QtWidgets.QPushButton("Нарисовать")
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(self.label)
        self.h_layout.addWidget(self.input)
        self.h_layout.addWidget(self.button)

        # layout для рисования
        self.print = QtWidgets.QLabel()
        self.canvas = QtGui.QPixmap(self.size())
        self.canvas.fill(QtGui.QColor("white"))
        self.print.setPixmap(self.canvas)
        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.addWidget(self.print)

        # Отображение созданных layout
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.h_layout)
        self.main_layout.addLayout(self.v_layout)

        # Назначаем функцию по нажатию
        self.button.clicked.connect(self.button_clicked)

    # Функция обработки кнопки для рисования
    def button_clicked(self): 
        # Обрабатываем ввод пользователя
        try:
            count = int(self.input.text())
            if count < 2 or count > 100: raise Exception()
        except:
            self.input.setText("Необходимо число! от 2 до 100 включительно")
            return  
        # Очищаем canvas от лишнего
        self.canvas.fill(QtGui.QColor("white"))
        self.print.setPixmap(self.canvas)
        # Вызываем функцию рисования линий
        self.draw_lines(count)

    def draw_lines(self, count = None):
        magic_number = 10
        painter = QtGui.QPainter(self.print.pixmap())

        # Настраиваем кисть для рисования
        brush = Qt.BDiagPattern
        painter.setBrush(brush)

        # Настраиваем ручку для рисования
        pen = QtGui.QPen()
        width_pen = magic_number - int(count/magic_number)
        print("размер линии", width_pen)
        pen.setWidth(width_pen)
        painter.setPen(pen)

        # Определяем максимальные размеры
        max_x = self.print.size().width()
        max_y = self.print.size().height()

        # Определяем расстояние между линиями
        plus_x = max_x / (count + 1)
        print("count", count)
        print("plus_x", plus_x)

        # Рисуем линии
        current_x = plus_x
        for number in range(count):
            point_x = QtCore.QPointF(current_x, magic_number)
            point_y = QtCore.QPointF(current_x, max_y - magic_number)
            painter.drawLine(QtCore.QLineF(point_x, point_y))
            current_x += plus_x
        
        # Рисуем прямоугольник со штриховкой
        start_x = QtCore.QPointF(plus_x, magic_number)
        rectangle = QtCore.QRectF(start_x, point_y)
        painter.drawRect(rectangle)

        self.update()
        painter.end()

def main():
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    window = Window()  # создаём объект класса ExampleApp
    window.show()  # показываем окно
    app.exec_()  # запускаем приложение

# Если файл запущен напрямую
if __name__ == '__main__':
    main()