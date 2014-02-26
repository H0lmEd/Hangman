from Tkinter import *
from random import randrange
import tkFont
import ttk

words = ["Elephant", "Purple", "Book", "Jazz"]

lives = 10
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
		self.wordFrame = ttk.Frame(mainframe)
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
		print (len(words),i,words)
		#words[i] = self.inputtedWord.get()
		for child in mainframe.winfo_children(): child.grid_forget()
		self.startPage()
		#pass
	def play(self):
		for child in mainframe.winfo_children(): child.grid_forget()
		i = randrange(0,len(words))
		global word
		word = words[i]
		print ("Word:", word)
		Leta = StringVar()
		self.canvas.grid(column=1, row=1, sticky=(N, W, E, S))
		self.wordFrame.grid(column=1, row=2)
		x2 = 1
		y2 = 1
		i = 0
		for ltr in word.lower():
			self.ltrLabel[i] = ttk.Label(self.wordFrame, text=" _ ")
			self.ltrLabel[i].grid(column=x2, row=y2)
			
			x2 += 2
			i += 1
		letterEntry = ttk.Entry(mainframe, textvariable=self.Leta, width=25)
		nextButton = ttk.Button(mainframe, text="Guess!", command=self.letterEntered)
		letterEntry.grid(column=1, row=3)
		nextButton.grid(column=2, row=3)

	def letterEntered(self):
		self.checkLetter()
	def checkLetter(self):
		self.letter = self.Leta.get()
		global lives	
		print ("LEta",self.Leta.get())
		if self.letter.lower() not in word.lower():
			lives -= 1
			if lives == 9:
				self.canvas.create_line(300, 200, 150, 200)
			if lives == 8:
				self.canvas.create_line(150, 200, 150, 50)
			if lives == 7:
				self.canvas.create_line(250, 50, 150, 50)
			if lives == 6:
				self.canvas.create_line(170, 50, 150, 70)
			if lives == 5:
				self.canvas.create_line(250, 50, 250, 65)
			if lives == 4:
				self.canvas.create_oval(235, 65, 265, 95)
			if lives == 3:
				self.canvas.create_line(250, 95, 250, 145)
			if lives == 2:
				self.canvas.create_line(230, 115, 270, 115)
			if lives == 1:
				self.canvas.create_line(250, 145, 235, 170)
			if lives == 0:
				self.canvas.create_line(250, 145, 265, 170)
				
		else:
			x = 0
			while x != len(word):
				
				if self.letter.lower() == word[x].lower():
					i = 0
					x2 = 1
					y2 = 1
					print (x, i)
					for ltr in word.lower():
						if self.showingLtr[i+1] == 0:
							pass
						else:
							self.ltrLabel[i].grid_forget()
						if ltr == self.letter.lower():
							self.showingLtr[i+1] = 0
							print ("They Match! X, Y",x,i)	
							self.ltrLabel[x] = ttk.Label(self.wordFrame, text=word[x].lower())
						else:
							print ("No match",i,x)
							self.ltrLabel[i] = ttk.Label(self.wordFrame, text=" _ ")
						self.ltrLabel[i].grid(column=x2, row=y2)
						x2 += 2
						i += 1
					#self.ltrLabel[x].grid_forget()	
					print (word[x], x)	
				print (x)
				print (len(word))
				x += 1
			print ("Leaving loop")
		print ("Lives remaining ", lives)

app = Application()
app.startPage()
root.mainloop()
