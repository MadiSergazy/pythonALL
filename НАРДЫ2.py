# -*- coding: utf-8 -*-
import random
#Definition of chessboard size
BOARD_SIZE = 15
#Define a two-dimensional list to serve as a chess board
board = []
def initBoard() :

    #Assign "*" to each element to draw a chess board on the console
    global row
    for i in range(BOARD_SIZE):
        row = ["*"] * BOARD_SIZE
        board.append(row)
    #Console output board method
def printBoard() :

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):

            print(board[i][j], end="")
        print()

initBoard()
printBoard()

import tkinter as tk

win = tk.Tk()
win.geometry("700x500+150+250")
win.title("НАРДЫ")



for i in range(15):
    for j in range(15):
        tk.Button(win, text=f'*').grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(1,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(2,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(3,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(4,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(5,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(6,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(7,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(8,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(9,  minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(10, minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(11, minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(12, minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(13, minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(14, minsize=40)  #индекс колонки, минимальны размер
win.grid_columnconfigure(15, minsize=40)  #индекс колонки, минимальны размер


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red')

# make_operation_button('O')
make_operation_button('O').grid(row= 1, column=0, stick='we', pady=0.5, padx=2)
make_operation_button("●").grid(row= 2, column=1, stick='we', pady=0.5, padx=2)










inputstr = input("Пожалуйста, введите координаты в формате x, y: \n" )
flag = False
while inputstr != None :
    x_str,y_str = inputstr.split(sep = ",")
    #Assign the value to the corresponding list "●"
    board[int(y_str)][int(x_str)] = "●"
    '''The computer randomly generates 2 integers as the coordinates of the computer, use "○" instead
         1. The validity of coordinates can only be a number, and cannot exceed the range of the board
         2. The point of playing chess cannot be repeated
         3. Every time you play chess you need to scan who won'''
    i = int(y_str)
    j = int(x_str)
    for x in range(j - 4 , j + 5) :
        if x >= 0 and x + 4 < 15 : #Horizontal whether there are 5 consecutively (traverse one by one at the edge, whether the five pieces are the same type)
            if board[i][x] == "●" and \
               board[i][x + 1] == "●" and \
               board[i][x + 2] == "●" and \
               board[i][x + 3] == "●" and \
               board[i][x + 4] == "●" :
               flag = True
               break
    for x in range(i - 4 , i + 5) :
        if x >= 0 and x + 4 < 15 : #Are there any 5 companies in the vertical direction (traverse one by one at the edge, whether the five pieces are the same type)
            if board[x][j] == "●" and \
               board[x + 1][j] == "●" and \
               board[x + 2][j] == "●" and \
               board[x + 3][j] == "●" and \
               board[x + 4][j] == "●" :
               flag = True
               break
    '''First determine the x-axis of the column of wins and losses under the diagonal of the northeast direction, y is the axis of the row,
         i is the row, j is the column (right diagonal) (traverse one by one at the edge, whether the five pieces are the same type)'''
    for x , y in zip(range(j + 4 , j-5 , -1 ),range(i - 4 , i + 5)) :
        if x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15 :
            if board[y][x] == "●" and \
               board[y - 1][x + 1] == "●" and \
               board[y - 2][x + 2] == "●" and \
               board[y - 3][x + 3] == "●" and \
               board[y - 4][x + 4] == "●" :
               flag = True
               break
    '''First determine the x-column axis in the diagonal of the northwest direction, y is the row axis,
         i is the row, j is the column (left diagonal) (traverse one by one at the edge, whether the five pieces are the same type)'''
    for x , y in zip(range(j - 4 , j+5  ),range(i - 4 , i + 5)) :
        if  x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15 :
            if board[y][x] == "●" and \
               board[y + 1][x + 1] == "●" and \
               board[y + 2][x + 2] == "●" and \
               board[y + 3][x + 3] == "●" and \
               board[y + 4][x + 4] == "●" :
               flag = True
               break
    if flag :
       printBoard()
       print("Congratulations, you won!")
       break
    from random import randint
    x_str1=random.randint(0,14)
    y_str1=random.randint(0,14)
    while board[int(y_str1)][int(x_str1)] == "●" or board[int(y_str1)][int(x_str1)] == "○" :
        x_str1=random.randint(0,14)
        y_str1=random.randint(0,14)
    board[int(y_str1)][int(x_str1)] = "○"
    printBoard()
    i = int(y_str1)
    j = int(x_str1)
    for x in range(j - 4 , j + 5) :
        if x >= 0 and x + 4 < 15 : #Horizontal whether there are 5 consecutively (traverse one by one at the edge, whether the five pieces are the same type)
            if board[i][x] == "○" and \
               board[i][x + 1] == "○" and \
               board[i][x + 2] == "○" and \
               board[i][x + 3] == "○" and \
               board[i][x + 4] == "○" :
               flag = True
               break
    for x in range(i - 4 , i + 5) :
        if x >= 0 and x + 4 < 15 : #Are there any 5 companies in the vertical direction (traverse one by one at the edge, whether the five pieces are the same type)
            if board[x][j] == "○" and \
               board[x + 1][j] == "○" and \
               board[x + 2][j] == "○" and \
               board[x + 3][j] == "○" and \
               board[x + 4][j] == "○" :
               flag = True
               break
    '''First determine the x-axis of the column of wins and losses under the diagonal of the northeast direction, y is the axis of the row,
         i is the row, j is the column (right diagonal) (traverse one by one at the edge, whether the five pieces are the same type)'''
    for x , y in zip(range(j + 4 , j-5 , -1 ),range(i - 4 , i + 5)) :
        if  x >= 0 and x + 4 < 15 and y + 4 >= 0 and y < 15 :
            if board[y][x] == "○" and \
               board[y - 1][x + 1] == "○" and \
               board[y - 2][x + 2] == "○" and \
               board[y - 3][x + 3] == "○" and \
               board[y - 4][x + 4] == "○" :
               flag = True
               break
    '''First determine the x-column axis in the diagonal of the northwest direction, y is the row axis,
         i is the row, j is the column (left diagonal) (traverse one by one at the edge, whether the five pieces are the same type)'''
    for x , y in zip(range(j - 4 , j+5  ),range(i - 4 , i + 5)) :
        if  x >= 0 and x + 4 < 15 and y >= 0 and y + 4 < 15 :
            if board[y][x] == "○" and \
               board[y + 1][x + 1] == "○" and \
               board[y + 2][x + 2] == "○" and \
               board[y + 3][x + 3] == "○" and \
               board[y + 4][x + 4] == "○" :
               flag = True
               break
    if flag :
       print("Sorry, you lost!")
       break
    inputstr = input("Please enter the coordinates of your game, in x, y format: \ n")


win.mainloop()


