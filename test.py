import tkinter as tk

SIZE = [4]

# print which button is clicked
def btn_click(i):
    print(f"clicked {i}")

# set size of grid according to the chosen difficulty option
def set_difficulty(diffOption):
    if diffOption == "easy":
        SIZE[0] = 4
    elif diffOption == "medium":
        SIZE[0] = 6
    elif diffOption == "hard":
        SIZE[0] = 8

    print(SIZE[0])
    draw(SIZE[0])


def draw(grid):
    btn_frame = tk.Frame(window)
    btn_frame.pack()
    
    for row in range(grid):
        for col in range(grid):
            i = (row,col)
            b = tk.Button(btn_frame, image=grid_img, command=lambda x=i: btn_click(x))
            b.grid(row=row + 1, column=col)



window = tk.Tk()
window.title("Quantun Minesweeper")
window.geometry("600x600")  # Set window size in px

menubar = tk.Menu(window)
window.config(menu=menubar)

difficulty_menu = tk.Menu(menubar)
difficulty_menu.add_command(label='Easy', command=lambda diffOption="easy": set_difficulty(diffOption))
difficulty_menu.add_command(label='Medium', command=lambda diffOption="medium": set_difficulty(diffOption))
difficulty_menu.add_command(label='Hard', command=lambda diffOption="hard": set_difficulty(diffOption))

menubar.add_cascade(label="Choose Difficulty", menu=difficulty_menu, underline=0)

grid_img = tk.PhotoImage(file = "images/Grid.png")

        
window.mainloop()