from tkinter import *
import random

BUTTON_HEIGHT = 1
BUTTON_WIDTH = 10

class Interface: 
    def __init__(self, window):
        self.mode = Frame(window)
        self.algorithms = Frame(window)
        self.userinput = Frame(window)
        self.exercises = Frame(window)
        self.answers = Frame(window)

        self.sortingAlgorithm = ""

        self.randomquestion, self.randomanswer = self.newQandA()
        self.resultmessage = None

        self.button1 = Button(self.mode, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Sorting", command = self.change_to_algorithms)
        self.button1.place(relx = 0.5, rely = 0.4, anchor = N)
        self.button2 = Button(self.mode, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Exercises", command = self.change_to_exercises)
        self.button2.place(relx = 0.5, rely = 0.5, anchor = N)

        self.button3a = Button(self.algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Bubblesort", command = lambda: self.change_to_userinput("Bubblesort"))
        self.button3a.place(relx = 0.5, rely = 0.1, anchor = N)
        self.button3b = Button(self.algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Insertionsort", command = lambda: self.change_to_userinput("Insertionsort"))
        self.button3b.place(relx = 0.5, rely = 0.2, anchor = N)
        self.button3c = Button(self.algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Selectionsort", command = lambda: self.change_to_userinput("Selectionsort"))
        self.button3c.place(relx = 0.5, rely = 0.3, anchor = N)
        self.button3d = Button(self.algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Mergesort", command = lambda: self.change_to_userinput("Mergesort"))
        self.button3d.place(relx = 0.5, rely = 0.4, anchor = N)
        self.button3e = Button(self.algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Quicksort", command = lambda: self.change_to_userinput("Quicksort"))
        self.button3e.place(relx = 0.5, rely = 0.5, anchor = N)
        self.button4 = Button(self.algorithms, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = self.change_to_mode)
        self.button4.place(relx = 0.5, rely = 0.6, anchor = N)

        self.button5 = Button(self.userinput, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "sort", command = self.change_to_blocksorting)
        self.button5.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.button6 = Button(self.userinput, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = self.change_to_algorithms)
        self.button6.place(relx = 0.5, rely = 0.6, anchor = N)
        self.entry = Entry(self.userinput, width = 40)
        self.entry.place(relx = 0.5, rely = 0.4, anchor = N)

        self.button7 = Button(self.exercises, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Check Answer", command = self.change_to_answers)
        self.button7.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.button8 = Button(self.exercises, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = self.change_to_mode)
        self.button8.place(relx = 0.5, rely = 0.6, anchor = N)
        self.answerbox = Entry(self.exercises, width = 40)
        self.answerbox.place(relx = 0.5, rely = 0.4, anchor = N)
        self.note = Label(self.exercises, text = "remember to use ^ for exponents")
        self.note.place(relx = 0.5, rely = 0.3, anchor = N)
        self.question = Label(self.exercises)
        self.question.place(relx = 0.5, rely = 0.35, anchor = N)

        self.button9 = Button(self.answers, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Next Question", command = self.change_to_exercises)
        self.button9.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        self.button10 = Button(self.answers, height = BUTTON_HEIGHT, width = BUTTON_WIDTH, text = "Back", command = self.change_to_mode)
        self.button10.place(relx = 0.5, rely = 0.6, anchor = N)
        self.result = Label(self.answers)
        self.result.place(relx = 0.5, rely = 0.4, anchor = N)

    def newQandA(self):
        f = open("QandA.txt", "r")
        lines = f.readlines()
        QandA = []
        for x in range(0, len(lines) - 1, 2):
            QandA.append([lines[x].replace("\n", ""), lines[x+1].replace("\n", "")])
        questionnumber = random.randint(0, len(QandA) - 1)
        randomquestion = QandA[questionnumber][0]
        randomanswer = QandA[questionnumber][1]
        return randomquestion, randomanswer
        
    def change_to_mode(self):
        self.mode.pack(fill='both', expand=1)
        self.algorithms.pack_forget()
        self.exercises.pack_forget()
        self.answers.pack_forget()

    def change_to_algorithms(self):
        self.entry.delete(0, "end")
        self.algorithms.pack(fill='both', expand=1)
        self.mode.pack_forget()
        self.userinput.pack_forget()

    def change_to_userinput(self, algorithm):
        self.sortingAlgorithm = algorithm
        self.userinput.pack(fill='both', expand=1)
        self.algorithms.pack_forget()

    def change_to_blocksorting(self):
        nodes = self.getelements()
        self.entry.delete(0, "end")
        self.userinput.pack_forget()
        self.change_to_algorithms()

    def change_to_exercises(self):
        self.exercises.pack(fill='both', expand=1)
        self.mode.pack_forget()
        self.answers.pack_forget()
        self.question.config(text = self.randomquestion)

    def change_to_answers(self):
        answer = self.answerbox.get().replace(" ","").replace("(", "").replace(")", "").replace("*", "").lower()
        self.answerbox.delete(0, "end")
        self.answers.pack(fill='both', expand=1)
        self.exercises.pack_forget()
        if answer == self.randomanswer:
            self.resultmessage = "Correct! Answer was " + self.randomanswer
        else:
            self.resultmessage = "Wrong! You put " + answer + " but the correct answer was " + self.randomanswer
        self.result.config(text = self.resultmessage)
        self.randomquestion, self.randomanswer = self.newQandA()
    
    def getelements(self):
        elements = self.entry.get()
        stripped = ""
        for char in elements:
            if char.isdigit():
                stripped = stripped + char
            else:
                stripped = stripped + ' '
        nodes = stripped.split()
        nodes = list(dict.fromkeys(nodes)) 
        inputlist = []
        for node in nodes:
            inputlist.append(int(node))
        print(inputlist)
        return inputlist

def main():
    window = Tk()
    window.title("Sorting Algorithms")
    window.geometry("1920x1080")
    interface = Interface(window)
    interface.change_to_mode()
    window.mainloop()

if __name__ =='__main__':
    main()