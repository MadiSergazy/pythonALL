# -- coding: utf-8 --
#программа дя сортировки файлов

from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):  #наследник от класса событии
    def on_modifided(self, event):     #срабатывает каждый раз при изменении в определенной папке
        for filename in os.listdir(folder_track): #мы перебераем все файлы в пути folder_track
            enterseption = filename.split(".")
            if len(enterseption) > 1 and (enterseption[1].lower() == 'jpg' or enterseption[1].lower() == 'png'):#сортируем их если расширения те что нам нужны
                file = folder_track + '\\' + filename  #
                new_path = folder_dest + '\\' + filename  #
                os.rename(file, new_path)  # переносим их в другую папку


folder_track = " "
folder_dest = " "

handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)

observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()