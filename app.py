# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QMessageBox
import threading
import requests
import init
import sys  
import os
import prog


class ExampleApp(QtWidgets.QMainWindow, prog.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_select.clicked.connect(self.select) 
        self.btn_save.clicked.connect(self.save)
        self.btn_enter.clicked.connect(self.enter)

    # Метод выбора файла
    def select(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(self, "Select file")
        if self.file != "":
            print(str(self.file[0]))
            self.line_file.setText(str(self.file[0]))
        else:
            pass

    # Метод выбора папки сохранения
    def save(self):
        self.file1 = QtWidgets.QFileDialog.getExistingDirectory(self, "Select file")
        if self.file1 != "":
            self.line_save.setText(self.file1)
        else:
            pass

    # Метод преобразования
    def enter(self):
        lang1 = ""
        if self.rbt_rus:
            lang1 = "рус"
        if self.rbt_eng:
            lang1 = "eng"

        if lang1 != "":
            img = Image.open(str(self.file[0]))

            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            TESSDATA_PREFIX = 'C:\Program Files\Tesseract-OCR\tessdata'
            file_name = img.filename
            file_name = file_name.split(".")[0]

            custom_config = r'--oem 3 --psm 6'
            text = pytesseract.image_to_string(img, lang= lang1, config= custom_config)
            print(text)
            form = "txt"

            with open(f'{file_name}.{form}', 'w') as text_file:
                text_file.write(text)
        else:
            pass



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()