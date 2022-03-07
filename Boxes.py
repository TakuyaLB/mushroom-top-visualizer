from cProfile import label
from pydoc import doc
import re
import tkinter as tk


root = tk.Tk()

width,height=1300,700 # set the variables 
c_width,c_height=width,height # canvas width height
d=str(width)+"x"+str(height)
root.geometry(d) 
canvas = tk.Canvas(root, width=c_width, height=c_height,bg='black')
canvas.pack()

x, y = 0, 0
box_length, box_width = 60, 60
space = 10

box_objects = {}
label_objects = {}

def draw_boxes(list_nums):
    n = len(list_nums)
    x,y = (c_width - ((box_length * n) + ((n - 1) * space))) // 2 , (c_height - box_width) // 2 
    for i in range (len(list_nums)):
        box = canvas.create_rectangle(x, y, (x + box_length), (y + box_width), fill= "red")
        label = canvas.create_text((x + (box_length//2), (y + (box_width // 2))), text=str(list_nums[i]))
        x += box_length + space
        box_objects [str(list_nums[i])] = box
        label_objects [str(list_nums[i])] = label

def find_n(key1, key2, temp_list):
    n = 0
    index = 0
    found = False
    while not found:
        if temp_list[index] != key1:
            del temp_list[0]
        else:
            del temp_list[0]
            found = True
    print(temp_list)
    found = False
    while not found:
        if temp_list[index] != key2:
            index += 1
            n += 1
        else:
            found = True

    return(n)

def move_down(key1, key2, x_speed, y_speed):
    global b_speed
    global b_move_down
    rect = box_objects.get(key1)
    lab = label_objects.get(key1)
    

    x1, y1, x2, y2 = canvas.coords(rect)
    # target_x1 = x1 + ((n+1)(box_length) + (n+1)(space))


    if y2 < c_height - 200:
        x_speed = 0
        y_speed = 5
    else:
        x_speed = 5 
        y_speed = 0

    canvas.move(rect, x_speed, y_speed)
    canvas.move(lab, x_speed, y_speed)

    # get current position        


    # check if you have to change direction
    #if b_speed > 0:
    if x2< c_width:
        canvas.after(25, lambda: move_down(key1, key2, x ,y))
    else:
        return 

b_speed = 5
b_move_down = True

def main():
    draw_boxes([4, 1, 8, 6, 2])
    
    n = find_n("1", "2", list(box_objects))
    print(n)

    move_down("1", "1", 0, 5)
    move_down("2", "2", 0, 5)



main()

root.mainloop()