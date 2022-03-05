from tkinter import *

BUTTON_HEIGHT = 1
BUTTON_WIDTH = 10

window = Tk()
window.title("Sorting Algorithms")
window.geometry("1920x1080")

mode = Frame(window)
algorithms = Frame(window)
userinput = Frame(window)

def change_to_mode():
    mode.pack(fill='both', expand=1)
    algorithms.pack_forget()

def change_to_algorithms():
    algorithms.pack(fill='both', expand=1)
    mode.pack_forget()
    userinput.pack_forget()

def change_to_userinput(algorithm):
    global sortingAlgorithm 
    sortingAlgorithm = algorithm
    userinput.pack(fill='both', expand=1)
    algorithms.pack_forget()

def exercises():
    pass

def getelements():
    elements = entry.get()
    stripped = ""
    for char in elements:
        if char.isdigit():
            stripped = stripped + char
        else:
            stripped = stripped + ' '
    global nodes
    nodes = stripped.split( )

button1 = Button(mode, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Sorting", command = change_to_algorithms)
button1.place(relx = 0.5, rely = 0.4, anchor = N)
button2 = Button(mode, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Exercises", command = exercises)
button2.place(relx = 0.5, rely = 0.5, anchor = N)

button3 = Button(algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Bubblesort", command = lambda: change_to_userinput("Bubblesort"))
button3.place(relx = 0.5, rely = 0.1, anchor = N)
button4 = Button(algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = change_to_mode)
button4.place(relx = 0.5, rely = 0.2, anchor = N)

button5 = Button(userinput, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "sort", command = getelements)
button5.place(relx = 0.5, rely = 0.5, anchor = CENTER)
button6 = Button(userinput, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = change_to_algorithms)
button6.place(relx = 0.5, rely = 0.6, anchor = N)
entry = Entry(userinput, width = 40)
entry.place(relx = 0.5, rely = 0.4, anchor = N)

change_to_mode()

window.mainloop()