from tkinter import *

root = Tk()
root.overrideredirect(1)
root.attributes("-topmost", True)
root.minsize(169,16)
canvas = Canvas(root, width=169, height=14)      
canvas.pack()      
img = PhotoImage(file="hypercamWatermark.gif")      
canvas.create_image(1, 0, anchor=NW, image=img)
mainloop()



