# -- coding: utf-8 --

import time          #
import numpy as np                #
import pyscreenshot as ImageGrab      #
import cv2                           #
import os                           #
import pytesseract                  #для чтения

# import pyautogui   #для того чтоб узнать координаты мышки   x=930, y=818     x=1336, y=916
# time.sleep(2)
# print(pyautogui.position()) #программа для показа позицыы координат нашей мыши по икс и игрик


filename = 'Image.png'    #путь к файлу
x = 1
last_time = time.time()

while (True):
    screen = np.array(ImageGrab.grab(bbox=(930, 818, 1336, 916)))   #области левый верхни и правый нижни
    print('loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))#программа сделает скриншотнеобходимой области экрана
    cv2.imwrite("SY" + filename, screen)#полученный файл будет с тем же именем что и в начале
    x = x + 1
    print(x)
    if x == 2:
        cv2.destroyAllWindows()
        break

img = cv2.imread('Image.png')   #читаем созданный нами файл картинку
text = pytesseract.image_to_string(img, lang='kaz') #даем данные в нейронную сеть для преобразавания в строку
print(text)

index = text.find("ФП")#ищем слово ФП
print(index)

if index == -1:
    print("ТАКОГО СЛОВА НЕТЬ!!!")
else:
    print("Я НАШЕЛЬ ЕНТО СЛОВО!!!")




