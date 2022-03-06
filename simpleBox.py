from textwrap import fill
from tkinter import *
import tkinter
from turtle import rt

# Canvas Setup
CANVAS_X = 600
CANVAS_Y = 600
root = tkinter.Tk()
root.title("Simple Box")
root.geometry(f"{CANVAS_X}x{CANVAS_Y}")
canvas = Canvas(root, width=CANVAS_X, height=CANVAS_Y, bg="white")
canvas.pack()

# Rectangle Setup
rectX1 = 50
rectY1 = CANVAS_Y // 2
rectX2 = rectX1 + 30
rectY2 = rectY1 + 30
rect1 = canvas.create_rectangle(rectX1, rectY1, rectX2, rectY2, fill = "red")

# Moves Functions
def move_right():
    canvas.move(rect1, 1, 0)
    root.after(25, move_right)

def move_up():
    canvas.move(rect1, 0, -1)
    root.after(25, move_up)

def move_left():
    canvas.move(rect1, -1, 0)
    root.after(25, move_left)


def move_down():
    canvas.move(rect1, 0, 1)
    root.after(20, move_down)



# if (rectX2 < CANVAS_X // 2):
#     move_right()
#     if (rectX2 == CANVAS_X // 2):
#         move_up()


root.mainloop()


# Previous Ideas

# step = 10
# x1, y1 = 20, int(CANVAS_Y/2)
# x2, y2 = x1 + 35, y1 + 35
# rect1 = canvas.create_rectangle(x1, y1, x2, y2, fill = "blue")

# def myDraw1():
#     global x1,y1,x2,y2,rect1
#     canvas.delete(rect1)
#     rect1 = canvas.create_rectangle(x1, y1, x2, y2, fill = "blue")

#     if (x2 < CANVAS_X // 2):
#         x1,x2 = x1 + step, x2 + step
#         canvas.after(100, myDraw1)
#     else:
#         return
# myDraw1()

# root.mainloop()

# bs = 20
# x_values = ['3', '4', '5', '6']
# y_values = ['11', '11', '11', '11']

# for x1,y1 in zip(x_values, y_values):
#     x1 = int(x1) * bs
#     y1 = int(y1) * bs
#     x2 = x1 + bs
#     y2 = y1 + bs
#     canvas.create_rectangle(x1,y1,x2,y2,fill="red")
#     canvas.create_text((x1,y1), text= listA[0])