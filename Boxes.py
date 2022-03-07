from cProfile import label
import re
import tkinter as tk


root = tk.Tk()

width,height=1000,800 # set the variables 
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

def move_down(r_key, l_key, x, y):
    global b_speed
    global b_move_down
    rect = box_objects.get(r_key)
    lab = label_objects.get(l_key)
    x1, y1, x2, y2 = canvas.coords(rect)

    if y2 < c_height - 200:
        x = 0
        y = 5
    else:
        x = 5 
        y = 0

    canvas.move(rect, x, y)
    canvas.move(lab, x, y)

    # get current position        
    print(y1, y2)

    # check if you have to change direction
    #if b_speed > 0:
    if x2< c_width:
        canvas.after(25, lambda: move_down(r_key, l_key, x ,y))
    else:
        return 

b_speed = 5
b_move_down = True

def main():
    draw_boxes([1,2,3,4,5,6,7,8])
    global x1, y1, x2, y2 
    x1, y1, x2, y2 = canvas.coords(box_objects.get("2"))
    move_down("2", "2", 0, 5)
    move_down("3", "3", 0, 5)
    # if x2 < c_width:
    # canvas.after(3000, move_right("2", "2"))
    # move_right("2", "2")
# move()

main()

root.mainloop()