from tkinter import *
import random

BUTTON_HEIGHT = 1
BUTTON_WIDTH = 10

window = Tk()
window.title("Sorting Algorithms")
window.geometry("1920x1080")

mode = Frame(window)
algorithms = Frame(window)
userinput = Frame(window)
exercises = Frame(window)
answers = Frame(window)

f = open("QandA.txt", "r")
lines = f.readlines()
global QandA
QandA = []
for x in range(0, len(lines) - 1, 2):
    QandA.append([lines[x].replace("\n", ""), lines[x+1].replace("\n", "")])

def change_to_mode():
    mode.pack(fill='both', expand=1)
    algorithms.pack_forget()
    exercises.pack_forget()
    answers.pack_forget()

def change_to_algorithms():
    algorithms.pack(fill='both', expand=1)
    mode.pack_forget()
    userinput.pack_forget()

def change_to_userinput(algorithm):
    global sortingAlgorithm 
    sortingAlgorithm = algorithm
    userinput.pack(fill='both', expand=1)
    algorithms.pack_forget()

def change_to_exercises():
    exercises.pack(fill='both', expand=1)
    mode.pack_forget()
    answers.pack_forget()
    global randomquestion
    global randomanswer
    questionnumber = random.randint(0, len(QandA) - 1)
    randomquestion = QandA[questionnumber][0]
    randomanswer = QandA[questionnumber][1]
    question.config(text = randomquestion)

def change_to_answers():
    answerbox.delete(0, "end")
    answers.pack(fill='both', expand=1)
    exercises.pack_forget()
    global resultmessage
    if answer == randomanswer:
        resultmessage = "Correct! Answer was " + randomanswer
    else:
        resultmessage = "Wrong! You put " + answer + " but the correct answer was " + randomanswer
    result.config(text = resultmessage)

def getanswer():
    global answer
    answer = answerbox.get().replace(" ","").replace("(", "").replace(")", "").replace("*", "").lower()
    change_to_answers()

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
button2 = Button(mode, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Exercises", command = change_to_exercises)
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

button7 = Button(exercises, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Check Answer", command = getanswer)
button7.place(relx = 0.5, rely = 0.5, anchor = CENTER)
button8 = Button(exercises, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = change_to_mode)
button8.place(relx = 0.5, rely = 0.6, anchor = N)
answerbox = Entry(exercises, width = 40)
answerbox.place(relx = 0.5, rely = 0.4, anchor = N)
note = Label(exercises, text = "remember to use ^ for exponents")
note.place(relx = 0.5, rely = 0.3, anchor = N)
question = Label(exercises)
question.place(relx = 0.5, rely = 0.35, anchor = N)

button9 = Button(answers, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Next Question", command = change_to_exercises)
button9.place(relx = 0.5, rely = 0.5, anchor = CENTER)
button10 = Button(answers, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = change_to_mode)
button10.place(relx = 0.5, rely = 0.6, anchor = N)
result = Label(answers)
result.place(relx = 0.5, rely = 0.4, anchor = N)

change_to_mode()

window.mainloop()