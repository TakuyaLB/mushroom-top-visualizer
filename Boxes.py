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

def move():
    global b_speed
    global b_move_down

    rect = box_objects.get("2")
    lab = label_objects.get("2")

    canvas.move(rect, 0, b_speed)
    canvas.move(lab, 0, b_speed)

    # get current position        
    x1, y1, x2, y2 = canvas.coords(rect)
    print(y1, y2)

    # check if you have to change direction
    #if b_speed > 0:
    if b_move_down:
        # if it reachs bottom
        if y2 > c_height:
            # change direction
            #b_move_down = False
            b_move_down = not b_move_down
            b_speed = -b_speed
    else:
        # if it reachs top
        if y1 < 0:
            # change direction
            #b_move_down = True
            b_move_down = not b_move_down
            b_speed = -b_speed

    # move again after 25 ms (0.025s)
    root.after(25, move)

def delete(num):
    string_num = str (num)
    canvas.delete(box_objects.get(string_num))
    canvas.delete(label_objects.get(string_num))

b_speed = 5
b_move_down = True

def main():
    draw_boxes([1,2,3,4,5,6,7,8])
    move()
# move()

main()

root.mainloop()