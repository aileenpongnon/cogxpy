# Aileen Pongnon
# CogxPy Project
# October 29, 2019  -

from tkinter import *
from tkinter.filedialog import askopenfilename

       # creates a blank window named "root" from Tk class
       # with the label text appearing in it
root = Tk()

def loadFile():
    print("Loading the file...")

       # creates a label on the screen
       # want this to be the loading button
buttonLoad = Button(root, text = "Load File", command = loadFile)
buttonLoad.pack()
labelOutput = Label(root, text = "Output: ")


entryLoad = Entry(root)
entryOutput = Entry(root)

buttonLoad.grid(row = 0)
labelOutput.grid(row = 1)

entryLoad.grid(row = 0, column = 1)
entryOutput.grid(row = 1, column = 1)
# label.pack()

root.mainloop()


# root = Tk()
# ftypes = [('csv file',"*.csv")]
# ttl = "Title"
# dir1 = 'C:\\'
# root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
# print(root.fileName)
