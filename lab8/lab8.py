import sys # Для передачи argv в QApplication
import lab8design # Конвертированный файл дизайна
from PyQt5 import QtWidgets
from collections import Counter
import string

class ExampleApp(QtWidgets.QMainWindow, lab8design.Ui_MainWindow):
    # Через данный метод происходит доступ к интерфейсу
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Это нужно для инициализации нашего дизайна 
        # Назначаем функции по нажатию кнопок
        self.button.clicked.connect(self.button_clicked)

    # Функция обработки кнопки для проверки анаграмм
    def button_clicked(self): 
        positive = "Данные предложения анаграммы"
        negative = "Данные предложения НЕ анаграммы"
        first = self.first_input.text()
        second = self.second_input.text()
        if self.is_anagram(first, second): self.output.setText(positive)
        else: self.output.setText(negative)

    def is_anagram(self, first = None, second = None):
        print(first, second)
        # Переводим предложения в нижний регистр
        first = first.lower()
        second = second.lower()
        print(first, second)
        # Удаляем из текста знаки пунктуации и пробел
        marks = string.punctuation + ' '
        for letter in marks: 
            first = first.replace(letter, '')
            second = second.replace(letter, '')
        print(first, second)
        # Проверка на соответствие длины
        if len(first) != len(second): return False
        # Преобразование в словарь подсчета
        first_counter = Counter(first)
        second_counter = Counter(second)
        print(first_counter, second_counter)
        # Возвращаем результат
        if first_counter == second_counter: return True
        else: return False

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

# Если файл запущен напрямую
if __name__ == '__main__':
    main()