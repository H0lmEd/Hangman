from tkinter import *
from random import randrange
import re
from tkinter import ttk

words = ["defrosted"]

lives = 6
root = Tk()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

class Application(Frame):
                
        def __init__(self):
                self.inputtedWord = StringVar()
                self.Leta = StringVar()
                self.canvas = Canvas(mainframe)
                self.ltrLabel = {}
                self.showingLtr = {}
                self.ltrVar = {}
                self.lives = StringVar()
                self.lives.set("6")
                self.wordFrame = ttk.Frame(mainframe)
                self.amountEntered = 0
                self.enteredLetters = []
                self.correctLetters = 0
        def startPage(self):
                ttk.Label(mainframe, text="Welcome To hangman!").grid(column=2, row=1, sticky=(N,S))
                ttk.Button(mainframe, text="Add word", command=self.addWordForm).grid(column=1, row=2, sticky=W)
                ttk.Button(mainframe, text="Play", command=self.play).grid(column=3, row=2, sticky=E)
                
        def addWordForm(self):
                for child in mainframe.winfo_children(): child.grid_forget()
                
                ttk.Entry(mainframe, textvariable=self.inputtedWord).grid(column=1, row=1, sticky=W)
                ttk.Button(mainframe, text="Add Word", command=self.addWord).grid(column=2, row=1, sticky=E)
        
        def addWord(self):
                i = len(words)+1
                inputWord = self.inputtedWord.get()
                if inputWord not in words:
                        words.append(inputWord)
                for child in mainframe.winfo_children(): child.grid_forget()
                self.startPage()
        def play(self):
                for child in mainframe.winfo_children(): child.grid_forget()
                i = randrange(0,len(words))
                global word
                word = words[i]
                Leta = StringVar()
                self.canvas.grid(column=3, row=1, sticky=(N, W, E, S))
                self.wordFrame.grid(column=3, row=2)
                x2 = 1
                y2 = 1
                i = 0
                for ltr in word.lower():
                        self.ltrVar[i] = StringVar()
                        self.ltrVar[i].set(' _ ')
                        self.ltrLabel[i] = ttk.Label(self.wordFrame, text=self.ltrVar[i].get())
                        self.ltrLabel[i].grid(column=x2, row=y2, sticky=(N, S))
                        x2 += 2
                        i += 1
                self.livesLabelName = ttk.Label(mainframe, text="Lives:")
                self.livesLabel = ttk.Label(mainframe, textvariable = self.lives)
                self.letterEntry = ttk.Entry(mainframe, textvariable=self.Leta, width=25)
                nextButton = ttk.Button(mainframe, text="Guess!", command=self.checkLetter)
                root.bind('<Return>', self.letterEntered)
                self.letterEntry.grid(column=3, row=4)
                self.livesLabelName.grid(column=1, row=4, sticky=E)
                self.livesLabel.grid(column=2, row=4, sticky=W)
                nextButton.grid(column=4, row=4) 
                self.letterEntry.focus()
        def letterEntered(self,count):
                
                self.checkLetter()
        
        def checkLetter(self):
                self.letter = self.Leta.get().lower()
                
                self.amountEntered +=1
                global lives
                self.letterEntry.delete(0, END)
                if not re.match("^[a-z]*$", self.letter):
                        top = Toplevel()
                        top.title("Alert")
                        ttk.Label(top, text="Please enter letters only").grid(column=1, row=1)
                        ttk.Button(top, text="Dismiss", command=top.destroy).grid(column=2,row=2)
                        top.focus()
                elif len(self.letter) > 1:
                        top = Toplevel()
                        top.title("Alert")
                        ttk.Label(top, text="Only enter one letter at a time!").grid(column=1, row=1)
                        ttk.Button(top, text="Dismiss", command=top.destroy).grid(column=2,row=2)
                        top.focus()
                elif self.letter in self.enteredLetters:
                        top = Toplevel()
                        top.title("Alert")
                        ttk.Label(top, text="Letter already entered! Please enter another").grid(column=1, row=1)
                        ttk.Button(top, text="Dismiss", command=top.destroy).grid(column=2,row=2)
                        top.focus()
                elif self.letter not in self.enteredLetters:
                        self.enteredLetters.extend(self.letter)
                        
                        if self.letter.lower() not in word.lower():
                                lives -= 1
                                self.lives.set(lives)
                                if lives == 5:
                                        self.canvas.create_line(300, 200, 150, 200)
                                        self.canvas.create_line(150, 200, 150, 50)
                                if lives == 4:
                                        self.canvas.create_line(250, 50, 150, 50)
                                        self.canvas.create_line(170, 50, 150, 70)
                                if lives == 3:
                                        self.canvas.create_line(250, 50, 250, 65)
                                        self.canvas.create_oval(235, 65, 265, 95)
                                if lives == 2:
                                        self.canvas.create_line(250, 95, 250, 145)
                                if lives == 1:                                        
                                        self.canvas.create_line(250, 145, 265, 170)

                                        self.canvas.create_line(250, 145, 235, 170)
                                if lives == 0:
                                        self.canvas.create_line(230, 115, 270, 115)
                                        top = Toplevel()
                                        top.title("Alert")
                                        ttk.Label(top, text="Game Over!").grid(column=1, row=1)
                                        ttk.Button(top, text="Ok", command=root.destroy).grid(column=2,row=2)
                                        top.focus()
                                
                        else:
                                x = 0
                                while x != len(word):
                                        y = 1
                                        if self.letter.lower() == word[x].lower():
                                                y=(x*2)+1
                                                self.ltrLabel[x].grid_forget()
                                                self.ltrLabel[x] = ttk.Label(self.wordFrame, text=self.letter.lower())
                                                self.ltrLabel[x].grid(column=y, row=1, sticky=(N,S))
                                                self.correctLetters += 1
                                                if self.correctLetters == len(word):
                                                        top = Toplevel()
                                                        top.title("Alert")
                                                        ttk.Label(top, text="Winner!!").grid(column=1, row=1)
                                                        ttk.Label(top, text="Your score: %s"%lives).grid(column=1, row=2)
                                                        ttk.Button(top, text="Ok", command=root.destroy).grid(column=2,row=3)
                                                        top.focus()
                                                y=(x*2)+1

                                        x += 1

app = Application()
app.startPage()
root.mainloop()

