from Tkinter import *
import tkFont
import ttk

word = "milk"

lives = 10
root = Tk()
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def main():
	app = Application(Leta.get())
	app.checkLetter()

class Application(Frame):
		
	def __init__(self, letter):
		self.letter = letter
		
	def checkLetter(self):
		global lives	
		print (self.letter)
		if self.letter.lower() not in word.lower():
			lives -= 1
			if lives == 9:
				canvas.create_line(300, 200, 150, 200)
			if lives == 8:
				canvas.create_line(150, 200, 150, 50)
			if lives == 7:
				canvas.create_line(250, 50, 150, 50)
			if lives == 6:
				canvas.create_line(170, 50, 150, 70)
			if lives == 5:
				canvas.create_line(250, 50, 250, 65)
			if lives == 4:
				canvas.create_oval(235, 65, 265, 95)
			if lives == 3:
				canvas.create_line(250, 95, 250, 145)
			if lives == 2:
				canvas.create_line(230, 115, 270, 115)
			if lives == 1:
				canvas.create_line(250, 145, 235, 170)
			if lives == 0:
				canvas.create_line(250, 145, 265, 170)
		else:
			x = 0
			while x != len(word):
				
				if self.letter.lower() == word[x].lower():
					#ltrLabel[x].grid_forget()
					#ltrLabel[x] = ttk.Label(wordFrame, text=word[x].lower(), font=customFont)
					ltrVar[x].set(word[x].lower())
					#ltrLabel[x].grid(row=1, column=x, sticky=E)	
					#ltrLabek[x].grid()
				print (x)
				print (len(word))
				x += 1
			print ("Leaving loop")
		print ("Lives remaining ", lives)
		#global lives
		

Leta = StringVar()

canvas = Canvas(mainframe)
canvas.grid(column=1, row=1, sticky=(N, W, E, S))

wordFrame = ttk.Frame(mainframe)
wordFrame.grid(column=1, row=2)

wordCanvas = Canvas(mainframe)
wordCanvas.grid(column=1, row=2)

customFont = tkFont.Font(family="Helvetica", size=20)
i = 0
x1 = 1
y1 = 1
ltrLabel = dict()
ltrVar = dict()
for ltr in word.lower():
	i += 1
	ltrVar[i] = StringVar()
	ltrVar[i].set("H")
	wordCanvas.create_text(x1, y1, text=ltr, font=customFont)
	#ltrLabel[i].grid(column=x1, row=y1, sticky=E)
	
	print (ltr, i)
	x1 += 1

letterEntry = ttk.Entry(mainframe, textvariable=Leta, width=25)
nextButton = ttk.Button(mainframe, text="Next", command=main)
letterEntry.grid(column=1, row=3)
nextButton.grid(column=2, row=3)



root.mainloop()
