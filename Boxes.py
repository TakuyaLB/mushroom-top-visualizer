from cProfile import label
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

# def move():
#     y = (c_height - box_width) // 2 
#     print(y)
#     if y >= 0:
#         canvas.move(box_objects.get("1"), 0, -1)
#         y -= 1
#         canvas.after(25, move())
#     else:
#         return


draw_boxes([1,2,3,4,5,6,7,8])
# move()


root.mainloop()