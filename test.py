import tkinter as tk

# print which button is clicked
def btn_click(i):
    print(f"clicked {i}")

def difficulty_easy():
    hide_all_frames()
    difficulty_easy_frame.pack(fill="both", expand=1)
    draw(4)

def difficulty_medium():
    hide_all_frames()
    difficulty_medium_frame.pack(fill="both", expand=1)
    draw(6)

def difficulty_hard():
    hide_all_frames()
    difficulty_hard_frame.pack(fill="both", expand=1)
    draw(8)

def draw(grid):
    if grid == 4:
        difficulty_frame = difficulty_easy_frame
    elif grid == 6:
        difficulty_frame = difficulty_medium_frame
    elif grid == 8:
        difficulty_frame = difficulty_hard_frame

    for row in range(grid):
        for col in range(grid):
            i = (row,col)
            b = tk.Button(difficulty_frame, image=grid_img, command=lambda x=i: btn_click(x))
            b.grid(row=row + 1, column=col)

def hide_all_frames():
    difficulty_easy_frame.pack_forget()
    difficulty_medium_frame.pack_forget()
    difficulty_hard_frame.pack_forget()


window = tk.Tk()
window.title("Quantun Minesweeper")
window.geometry("600x600")  # Set window size in px

menubar = tk.Menu(window)
window.config(menu=menubar)

difficulty_menu = tk.Menu(menubar)
menubar.add_cascade(label="Choose Difficulty", menu=difficulty_menu)
difficulty_menu.add_command(label='Easy', command=difficulty_easy)
difficulty_menu.add_command(label='Medium', command=difficulty_medium)
difficulty_menu.add_command(label='Hard', command=difficulty_hard)

#Create some frames
difficulty_easy_frame = tk.Frame(window, width=600, height=600, bg="red")
difficulty_medium_frame = tk.Frame(window, width=600, height=600, bg="blue")
difficulty_hard_frame = tk.Frame(window, width=600, height=600, bg="black")

grid_img = tk.PhotoImage(file = "images/Grid.png")

        
window.mainloop()