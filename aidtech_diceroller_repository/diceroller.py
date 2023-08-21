import tkinter as tk
from tkinter import *
import random
from PIL import Image, ImageTk

w = tk.Tk()
w.title("DICE ROLLER")
w.geometry("393x400")  # Adjust the window width to fit all images

# Load dice images and store references globally
dice_images = {
    1: ImageTk.PhotoImage(Image.open("d1.png")),
    2: ImageTk.PhotoImage(Image.open("d2.png")),
    3: ImageTk.PhotoImage(Image.open("d3.png")),
    4: ImageTk.PhotoImage(Image.open("d4.png")),
    5: ImageTk.PhotoImage(Image.open("d5.png")),
    6: ImageTk.PhotoImage(Image.open("d6.png"))
}
dice_labels = []
def roll():
    
    
    num_rolls = int(roll_input.get())
    for label in dice_labels:
        label.destroy()
    dice_labels.clear()


    for i in range(num_rolls):
        a = random.randint(1, 6)
        dice_label = tk.Label(dice_frame, image=dice_images[a])
        dice_label.pack(side="left", padx=10)  # Adjust spacing between images
        dice_labels.append(dice_label) 
        print(a)



roll_label = tk.Label(w, text="Enter number of rolls:",font="Times 20")
roll_label.pack()

roll_input = tk.Entry(w,font="Times 20")
roll_input.pack()

Button(w,text="JUST A ROLL",fg="white",bg="indigo",font="Times 15",bd=10,command=roll).pack()

dice_frame = tk.Frame(w)
dice_frame.pack()


im1=ImageTk.PhotoImage(Image.open("ground.jpeg"))
Label(w,image=im1).place(x=0,y=250)


w.mainloop()


