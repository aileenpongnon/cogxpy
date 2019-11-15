# Aileen Pongnon
# CogxPy Project
# October 29, 2019  - November 15, 2019

from tkinter import *
from tkinter import filedialog

# creates window from Tk class, titled CogxPy
root = Tk()
root.title('CogxPy')

# declaring ftypes
ftypes = [('csv file',"*.csv"), ("txt files", "*.txt")]

# modifying position of frame on the screen
root.geometry("+500+250")

def loadFile():
    print("Loading the file...")
    root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = ftypes)
    print(root.filename)

       # want this to be the loading button
buttonLoad = Button(root, text = "Load File", command = loadFile)
labelOutput = Label(root, text = "Output: ")
# labelLoad = Label(root, text = ".csv")

entryLoad = Entry(root)
# want this to be input from code instead
entryOutput = Entry(root)

buttonLoad.grid(row = 0, padx = 50, pady = 100)
labelOutput.grid(row = 1)

entryLoad.grid(row = 0, column = 1, padx = 50)
entryOutput.grid(row = 1, column = 1, pady = 100)

root.mainloop()
