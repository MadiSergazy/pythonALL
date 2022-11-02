from tkinter import *


# Define a chess board with an array, the board size is 15×15
# Array index represents position,
# Element value represents the state of the position: -1 means no chess piece, 0 means black chess, 1 means white chess.

def callback(event):
    global tag, tagx, tagy, a
    color = ["black", "white"]
    x = round(event.x / mesh) - 1
    y = round(event.y / mesh) - 1
    errorX = mesh * (x + 1) - event.x
    errorY = mesh * (y + 1) - event.y
    dis = (errorX ** 2 + errorY ** 2) ** 0.5
    if QP[x][y] == -1 and dis < K / 2 * mesh and stop == 0:
        a.config(text=key[(tag + 1) % 2], fg=color[(tag + 1) % 2])
        QP[x][y] = tag
        canvas.create_oval(mesh * (x + 1) - Qr, mesh * (y + 1) - Qr, mesh * (x + 1) + Qr, mesh * (y + 1) + Qr,
                           fill=color[tag])
        v = [[0, 1], [1, 0], [1, 1], [1, -1]]
        for i in v:
            x1, y1 = x, y
            while x1 < num - 1 and x1 > 0 and y1 > 0 and y1 < num - 1:
                x1 += i[0]
                y1 += i[1]
            count = 0
            while x1 <= num - 1 and x1 >= 0 and y1 >= 0 and y1 <= num - 1:
                if QP[x1][y1] == tag:
                    count += 1
                    if count == 5:
                        win()
                else:
                    count = 0
                x1 -= i[0]
                y1 -= i[1]
        tag = (tag + 1) % 2
        tagx, tagy = x, y


def restart():
    global QP, tag, a, b, stop
    QP = []
    for i in range(num):
        QP.append([-1] * num)
    canvas.create_rectangle(mesh - 20, mesh - 20, mesh * num + 20, mesh * num + 20, fill="yellow")
    for i in range(num):
        canvas.create_line(mesh, mesh * (i + 1), mesh * num, mesh * (i + 1))
        canvas.create_line(mesh * (i + 1), mesh, mesh * (i + 1), mesh * num)
    tag = 0
    stop = 0
    a.config(text=key[tag], fg=color[tag])
    b.config(text="Go", fg=color[tag])


def regret():
    if stop != 1:
        QP[tagx][tagy] = -1
        x, y = tagx, tagy
        # The trouble here is mainly because the drawing function of tkinter egg pain is not powerful enough.
        # There is no way to set the color of the border of the chess pieces, it will leave a mark after regretting the chess.

        # At the chess piece, cover it with yellow first
        canvas.create_rectangle(mesh * (x + 1) - Qr, mesh * (y + 1) - Qr, mesh * (x + 1) + Qr, mesh * (y + 1) + Qr,
                                fill="yellow")
        # Draw a yellow line at the black border
        canvas.create_line(mesh * (x + 1) - Qr, mesh * (y + 1) - Qr, mesh * (x + 1) - Qr, mesh * (y + 1) + Qr,
                           fill="yellow")
        canvas.create_line(mesh * (x + 1) - Qr, mesh * (y + 1) + Qr, mesh * (x + 1) + Qr, mesh * (y + 1) + Qr,
                           fill="yellow")
        canvas.create_line(mesh * (x + 1) + Qr, mesh * (y + 1) + Qr, mesh * (x + 1) + Qr, mesh * (y + 1) - Qr,
                           fill="yellow")
        canvas.create_line(mesh * (x + 1) + Qr, mesh * (y + 1) - Qr, mesh * (x + 1) - Qr, mesh * (y + 1) - Qr,
                           fill="yellow")
        # Finally draw the chess line
        canvas.create_line(mesh * (x + 1), mesh * (y + 1) - mesh / 2, mesh * (x + 1), mesh * (y + 1) + mesh / 2)
        canvas.create_line(mesh * (x + 1) - mesh / 2, mesh * (y + 1), mesh * (x + 1) + mesh / 2, mesh * (y + 1))


def lose():
    global stop
    a.config(text=key[tag], fg=color[tag])
    b.config(text="confess", fg='black')
    stop = 1  # stop = 1 can no longer place pieces


def win():
    global stop
    a.config(text=key[tag], fg=color[tag])
    b.config(text="Win", fg='red')


stop = 1

if __name__ == '__main__':
    tag = 0  # tag marks which round to go, 0 represents black, 1 represents white
stop = 0
num = 18  # Number of checkerboard grids
K = 0.9  # The sensitivity of click is between 0~1
Qr = 0.45  # The size of the piece, the previous coefficient is selected between 0~0.5

px = 5
py = 50
wide = 60
high = 30
mesh = round(400 / num)
key = ["Black Party", "White Party"]
color = ["black", "white"]

# Initialize the board
QP = []
for i in range(num):
    QP.append([-1] * num)

tk = Tk()
tk.geometry(str((num + 1) * mesh + 2 * px) + 'x' + str((num + 1) * mesh + py + px))
tk.title('Gobang')
# Construct chess board interface
asdf = Canvas(tk, width=(num + 1) * mesh + 2 * px, height=(num + 1) * mesh + py + px)
asdf.place(x=0, y=0)
asdf.create_rectangle(0, 0, (num + 1) * mesh + 2 * px, (num + 1) * mesh + py + px, fill="green")
canvas = Canvas(tk, width=str((num + 1) * mesh), height=str((num + 1) * mesh))
canvas.place(x=px, y=py)
canvas.create_rectangle(mesh - 20, mesh - 20, mesh * num + 20, mesh * num + 20, fill="yellow")
for i in range(num):
    canvas.create_line(mesh, mesh * (i + 1), mesh * num, mesh * (i + 1))
    canvas.create_line(mesh * (i + 1), mesh, mesh * (i + 1), mesh * num)
canvas.bind("<Button-1>", callback)

# A few buttons
Button(tk, text='start', command=restart).place(x=2 * px, y=(py - high) / 2, width=wide, heigh=high)
Button(tk, text='recome', command=restart).place(x=2 * px + 60 + 10, y=(py - high) / 2, width=wide, heigh=high)
Button(tk, text='regret chess', command=regret).place(x=(num + 1) * mesh + px - wide - px - 60 - 10, y=(py - high) / 2,
                                                      width=wide, heigh=high)
Button(tk, text='confess', command=lose).place(x=(num + 1) * mesh + px - wide - px, y=(py - high) / 2, width=wide,
                                               heigh=high)

# Center text
a = Label(tk, text=key[tag], fg=color[tag], bg='green', font=("Times", "14", "bold"))
b = Label(tk, text="Go", fg=color[tag], bg='green', font=("Times", "14", "bold"))
a.place(x=2 * px + 60 + 10 + 90, y=(py - high) / 2 + 4)
b.place(x=(num + 1) * mesh + px - wide - px - 10 - 42 - 90, y=(py - high) / 2 + 4)

tk.mainloop()