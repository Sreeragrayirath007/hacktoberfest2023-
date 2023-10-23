# Not completed

from tkinter import *
from PIL import ImageTk, Image
import os

num =0
FOLDER = r'C:\Users\suyash\Desktop\VLSI\2'
FOLDER = FOLDER.replace('\\', '/')

os.chdir(FOLDER)
nam = os.listdir()
img = [] 
for x in nam:
    loc = FOLDER + '/' + x
    img.append(ImageTk.PhotoImage(Image.open(loc))) 

def change(val, lb, img):
    global num
    num = num + val
    lb.grid_forget()
    lb = Label(image=img[num])
    lb.grid(row=0, column=0, columnspan=3)
    return lb
    

def main():
    root = Tk()
    root.title("Icon, Image and Exit")
        
    lb = Label(image=img[0])
    lb.grid_forget()

    # Making of button
    btn_back = Button(root, text='<=', command = lambda: change(-1, lb, img))
    btn_quit = Button(root, text='Quit', command=root.quit)
    btn_ford = Button(root, text='=>',command =lambda: change(1, lb, img))

    btn_back.grid(row=1, column=0)
    btn_quit.grid(row=1, column=1)
    btn_ford.grid(row=1, column=2)

    root.mainloop()

main()
