# Aileen Pongnon
# CogxPy Project
# October 29, 2019  -

from tkinter import *
from tkinter.filedialog import askopenfilename

       # creates a blank window named "root" from Tk class
       # with the label text appearing in it
# root = Tk()
#        # creates a label on the screen
# label = Label(root, text = "Here's some text!")
# label.pack()
#
# root.mainloop()

root = Tk()
ftypes = [('txt file',"*.txt")]
ttl = "Title"
dir1 = 'C:\\'
root.fileName = askopenfilename(filetypes = ftypes, initialdir = dir1, title = ttl)
print(root.fileName)

#tdgrhfjgku
