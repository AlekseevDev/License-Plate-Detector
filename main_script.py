# -*- coding: utf-8 -*-
# Импортируем библиотеки
import os
import cv2
from tkinter import *
from tkinter import filedialog

# Создаем графический интерфейс для удобного указания расположения фото
def open_picture():
    root = Tk()
    root.withdraw()
    file_name = filedialog.askopenfilename(title="Select your photo")
    return file_name


# определяем папку и загружаем наше фото и модель (каскад)
pic = open_picture()
folder = "detecting_result"
image = cv2.imread(pic)
face_cascade = cv2.CascadeClassifier('cascade_russian_plate_number.xml')

# работаем на фото, изменяем его для лучшего нахождения номера
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(10, 10)
)

# ищем номер по заданым ранее параметрам и расставляем рамку
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)

# сохраняем фото с выделеными номерными знаками в папку
if os.path.exists(folder):
    cv2.imwrite(os.path.join(folder, pic), image)
else:
    os.mkdir(folder)
    cv2.imwrite(os.path.join(folder, pic), image)
    
# выводим фото на экран
cv2.imshow("Result", image)
cv2.waitKey(0)
