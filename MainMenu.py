from tkinter import *
from tkinter import font
import QuantumGame as qg

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

# Create two frames in the window
easy_option = Frame(win)
medium_option = Frame(win)
hard_option = Frame(win)

# Define a function for switching the frames
def easy_frame():
    hide_all_frames()
    easy_option.pack(fill='both', expand=1)
    minesweeper = qg.Minesweeper(easy_option, 4)


def medium_frame():
    hide_all_frames()
    medium_option.pack(fill='both', expand=1)
    label2 = Label(medium_option, text="test", foreground="blue")
    label2.pack(pady=20)
    minesweeper = qg.Minesweeper(medium_option, 6)

def hard_frame():
    hide_all_frames()
    hard_option.pack(fill='both', expand=1)
    minesweeper = qg.Minesweeper(hard_option, 8)

def hide_all_frames():
    easy_option.pack_forget()
    medium_option.pack_forget()
    hard_option.pack_forget()

win.title("Quantum Minesweeper")

btn1 = Button(win, text="Easy", command=easy_frame).pack()
btn2 = Button(win, text="Medium", command=medium_frame).pack()
btn3 = Button(win, text="Hard", command=hard_frame).pack()


win.mainloop()