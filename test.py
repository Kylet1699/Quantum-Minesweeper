import tkinter as tk

# print which button is clicked
def btn_click(i,difficulty_frame):
    print(f"clicked {i}")
    (row,col) = i
    bomb_prediction(row,col,difficulty_frame)


def difficulty_easy():
    hide_all_frames()
    difficulty_easy_frame.pack(fill="both", expand=1)
    difficulty_frame = difficulty_easy_frame
    draw(4, difficulty_frame)

def difficulty_medium():
    hide_all_frames()
    difficulty_medium_frame.pack(fill="both", expand=1)
    difficulty_frame = difficulty_medium_frame
    draw(6,difficulty_frame)

def difficulty_hard():
    hide_all_frames()
    difficulty_hard_frame.pack(fill="both", expand=1)
    difficulty_frame = difficulty_hard_frame
    draw(8,difficulty_frame)

# Draw grid
def draw(grid,difficulty_frame):
    for row in range(grid):
        for col in range(grid):
            i = (row,col)
            b = tk.Button(difficulty_frame, image=grid_img, command=lambda x=i: btn_click(x,difficulty_frame))
            b.grid(row=row + 1, column=col)


def hide_all_frames():
    difficulty_easy_frame.pack_forget()
    difficulty_medium_frame.pack_forget()
    difficulty_hard_frame.pack_forget()


# check if location of the button clicked is a bomb
def is_bomb(x,y):
    bomb_loc = [(0,0), (1,0), (2,1)]    # Test with bomb locations

    if (x,y) in bomb_loc:
        return True
    else:
        return False

def bomb_prediction(row,col, difficulty_frame):
    i = (row,col)
    if is_bomb(row,col):
        bomb_tester_predict_label = tk.Label(difficulty_frame, text="Bomb tester says there is a bomb.")
        bomb_tester_predict_label.grid(column=10, row=1, padx=5, pady=5)
        b = tk.Button(difficulty_frame,image=bomb_img, command=lambda x=i: btn_click(x))
        b.grid(row=row + 1, column=col)
    else:
        bomb_tester_predict_label = tk.Label(difficulty_frame, text="Bomb tester says there is no bomb.")
        bomb_tester_predict_label.grid(column=10, row=1, padx=5, pady=5)
        b = tk.Button(difficulty_frame,image=no_bomb_img, command=lambda x=i: btn_click(x))
        b.grid(row=row + 1, column=col)
    


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
bomb_img = tk.PhotoImage(file = "images/mineClicked.png")
no_bomb_img = tk.PhotoImage(file = "images/empty.png")

        
window.mainloop()