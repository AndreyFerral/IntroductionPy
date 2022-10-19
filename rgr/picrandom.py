from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Отображаем картинки")
        self.setFont(QtGui.QFont('Arial', 12))
        max_x, max_y = 500, 500
        self.resize(max_x, max_y)

        # Горизонтальный layout
        self.label = QtWidgets.QLabel("Номер картинки")
        self.spin = QtWidgets.QSpinBox()
        self.spin.setAlignment(QtCore.Qt.AlignCenter)
        self.spin.setMinimum(1)
        self.spin.setMaximum(10)
        self.h_layout = QtWidgets.QHBoxLayout()
        self.h_layout.addWidget(self.label, stretch=3)
        self.h_layout.addWidget(self.spin, stretch=1)

        # layout для отображения картинок
        self.picture = QtWidgets.QLabel()
        self.v_layout = QtWidgets.QVBoxLayout()
        self.v_layout.addWidget(self.picture)

        # Отображение созданных layout
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.addLayout(self.h_layout)
        self.main_layout.addLayout(self.v_layout)

        # Первоначальная настройка отображения
        self.change_pic(max_x, max_y)
        # Назначаем функцию по изменению значения
        self.spin.valueChanged.connect(lambda: self.change_pic(max_x, max_y))

    # Функция обработки кнопки для отображения картинок
    def change_pic(self, max_x = None, max_y = None): 
        pic_name = str(self.spin.value())
        pic_path = "rgr/pics/" + pic_name + ".png"
        pixmap = QtGui.QPixmap(pic_path)
        pixmap = pixmap.scaled(max_x, max_y)
        self.picture.setPixmap(pixmap)

def main():
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    window = Window()  # создаём объект класса ExampleApp
    window.show()  # показываем окно
    app.exec_()  # запускаем приложение

# Если файл запущен напрямую
if __name__ == '__main__':
    main()