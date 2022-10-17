import sys # для передачи argv в QApplication
import ui_lab6 # файл дизайна
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow, ui_lab6.Ui_MainWindow):
    # Через данный метод происходит доступ к интерфейсу
    def __init__(self):
        super().__init__()
        self.setupUi(self) # инициализации дизайна
        # Назначаем функции по нажатию кнопок
        self.year_button.clicked.connect(self.year_button_clicked)
        self.figure_button.clicked.connect(self.figure_button_clicked)

    # Функция обработки кнопки китайского гороскопа
    def year_button_clicked(self): 
        try:
            text = self.chinese_horoscope(int(self.year_input.text()))
        except:
            self.year_output.setText("Необходимо число!")
            return     
        self.year_output.setText(text)
    
    # Функция обработки кнопки фигуры
    def figure_button_clicked(self): 
        try:
            text = self.guess_shape(int(self.figure_input.text()))
        except:
            self.figure_output.setText("Необходимо число!")
            return   
        self.figure_output.setText(text)

    def chinese_horoscope(self, year = None):
        result = None
        match year%12:
            case 0: result = "Год обезьяны"
            case 1: result = "Год петуха"
            case 2: result = "Год собаки"
            case 3: result = "Год свиньи"
            case 4: result = "Год крысы"
            case 5: result = "Год быка"
            case 6: result = "Год тигра"
            case 7: result = "Год кролика"
            case 8: result = "Год дракона"
            case 9: result = "Год змеи"
            case 10: result = "Год лошади"
            case 11: result = "Год козы"
        return result
    
    def guess_shape(self, count = None):
        result = None
        if count == 3: result = "Треугольник"
        elif count == 4: result = "Четырехугольник"
        elif count == 5: result = "Пятиугольник"
        elif count == 6: result = "Шестиугольник"
        elif count == 7: result = "Семиугольник"
        elif count == 8: result = "Восьмиугольник"
        elif count == 9: result = "Неугольник"
        elif count == 10: result = "Десятиугольник"
        else: result = "Количество сторон должно быть от 3 до 10 включительно"
        return result

def main():
    app = QtWidgets.QApplication(sys.argv)  # новый экземпляр QApplication
    window = ExampleApp()  # создаём объект класса ExampleApp
    window.show()  # показываем окно
    app.exec_()  # запускаем приложение

# Если файл запущен напрямую
if __name__ == '__main__':
    main()