# Aileen Pongnon
# CogxPy Project
# October 29, 2019  -

from tkinter import *
from tkinter.filedialog import askopenfilename

# creates window from Tk class, titled CogxPy
root = Tk()
root.title('CogxPy')

# modifying position of frame on the screen
root.geometry("+500+250")

def loadFile():
    print("Loading the file...")

       # want this to be the loading button
buttonLoad = Button(root, text = "Load File", command = loadFile)
labelOutput = Label(root, text = "Output: ")

entryLoad = Entry(root)
# want this to be input from code instead
entryOutput = Entry(root)

buttonLoad.grid(row = 0, padx = 50, pady = 100)
labelOutput.grid(row = 1)

entryLoad.grid(row = 0, column = 1, padx = 50)
entryOutput.grid(row = 1, column = 1, pady = 100)

root.mainloop()

# root = Tk()
# ftypes = [('csv file',"*.csv")]
# ttl = "Title"
# dir1 = 'C:\\'
# root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
# print(root.fileName)
