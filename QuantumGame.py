from tkinter import *
from turtle import xcor
import TextUI as tui
import BombTester as bt
import numpy as np
from collections import deque

window = None

# SIZE = 10

BTN_CLICK = "<Button-1>"

class Minesweeper:
    size = 4
    def __init__(self, tk, size):
        self.curr_tile = None
        self.score = 0
        self.size = size

        # Images
        self.images = {
            "plain": PhotoImage(file = "images/Grid.png"),
            "no_bomb": PhotoImage(file = "images/empty.png"),
            "bomb": PhotoImage(file = "images/mineClicked.png"),
        }

        # Set up frame
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()

        # set up UI
        self.labels = {
            "prediction": Label(self.frame, text = "Quantum bomb tester says"),
            "buttons": {
                "yes_btn": Button(self.frame, text = "Yes", command = lambda x = self.curr_tile: self.updateTile(self.curr_tile, 1)),
                "no_btn": Button(self.frame, text = "No", command = lambda x = self.curr_tile: self.updateTile(self.curr_tile, 0))
            },
            "score": Label(self.frame, text = "Correct guesses " + str(self.score))
        }

        # Place UI at the bottom
        self.labels["prediction"].grid(row = 11, column = 0, columnspan = 10)
        self.labels["buttons"]["yes_btn"].grid(row = 12, column = 0, columnspan = 5)
        self.labels["buttons"]["no_btn"].grid(row = 12, column = 6, columnspan = 5)
        self.labels["score"].grid(row = 13, column = 0, columnspan = 10)
        
        self.restart(size)

    def setup(self,size):
        # Create list of dictionary objects of the game seed
        self.game_seed = dict({})
        self.score = 0

        # Initialize tile/button for the grid 
        for x in range(size):
            for y in range(size):
                if y == 0:
                    self.game_seed[x] = {}

                # Initialize the game with 3 beamsplitters
                this_seed = bt.get_count(3)[0] # Returns a string of qubits

                x_y = str(x) + "_" + str(y)
                
                # Each tile hold its info
                seed = {
                    "id": this_seed,
                    "bomb_qubit": this_seed[0],
                    "detector_qubit": this_seed[1],
                    "beam_splitters": 3,
                    "coords": {
                        "x": x,
                        "y": y
                    },
                    "state": 0, # 0 not clicked, 1 clicked
                    "x_y": x_y,
                    "button": Button(self.frame, image = self.images["plain"])
                }

                # Place button on the grid
                seed["button"].grid(row = x, column = y)
                # Make button interactable
                seed["button"].bind(BTN_CLICK, self.showPredictionWrapper(seed))

                # Add this seed to the list of game seeds
                self.game_seed[x][y] = seed


    # Restart game
    def restart(self,size):
        self.setup(size)
    
    def showPredictionWrapper(self, seed):
        return lambda Button: self.showPrediction(seed)

    # Displays bomb detector prediction
    def showPrediction(self, seed):
        # Check number of revealed neighbours and generate new seed with 3 + (2 * n) beam splitters
        neighbours = self.getNeighbours(seed["coords"]["x"], seed["coords"]["y"])
        revealed_neighbours = 0
        for i in neighbours:
            if i["state"] == 1:
                revealed_neighbours += 1
        
        x = seed["coords"]["x"]
        y = seed["coords"]["y"]
        new_beam_splitters = 3 + 2 * revealed_neighbours
        new_seed = bt.get_count(new_beam_splitters)[0]
        self.game_seed[x][y]["beam_splitters"] = new_beam_splitters
        self.game_seed[x][y]["bomb_qubit"] = new_seed[0]
        self.game_seed[x][y]["detector_qubit"] = new_seed[1]

        # Get probability
        probability_dist = bt.get_probability(new_beam_splitters)
        probability = probability_dist['01' + '0' * (new_beam_splitters - 1)] + probability_dist['1' + '0' * (new_beam_splitters)]

        print(seed) # show tile info in command line for testing purposes

        self.curr_tile = seed
        if seed["detector_qubit"] == '1':
            self.labels["prediction"].configure(text = "Quantum bomb tester says there is no bomb (." + str(probability) + ")")
        else:
            self.labels["prediction"].configure(text = "Quantum bomb tester says there is a bomb (." + str(probability) + ")")

    # Update tile after user input
    def updateTile(self, tile, input):
        if input == int(tile["bomb_qubit"]):
            self.labels["prediction"].configure(text = "Congratz, you predicted correctly")
            self.score += 1
            self.labels['score'].configure(text = "Correct guesses " + str(self.score))
        else:
            self.labels["prediction"].configure(text = "Oops, you predicted wrong")
            self.restart()

        if tile['bomb_qubit'] == '1':
            tile['button'].configure(image = self.images['bomb'])
            tile['state'] = 1
        else:
            tile['button'].configure(image = self.images['no_bomb'])
            tile['state'] = 1
            self.clearSurroundingTiles(tile["x_y"])

        tile['button'].unbind(BTN_CLICK)

        self.checkGameBoard()

    def checkGameBoard(self):
        clicked_tile_count = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.game_seed[x][y]["state"] == 1:
                    clicked_tile_count += 1
        if clicked_tile_count == (self.size**2):
            self.restart() 


    # Deque surrounding tiles recursively
    def clearSurroundingTiles(self, x_y):
        queue = deque([x_y])

        # Pop item off of queue and gets its coords
        while len(queue) != 0:
            key = queue.popleft()
            parts = key.split("_")
            x = int(parts[0])
            y = int(parts[1])

            # Clears surround tile to see if it has bomb
            for tile in self.getNeighbours(x, y):
                self.clearTile(tile, queue)

    # Check if tile has bomb, if not, add tile to queue
    def clearTile(self, tile, queue):
        if tile["state"] == 1:
            return

        if tile["bomb_qubit"] == '0':
            tile["button"].configure(image = self.images['no_bomb'])
            tile["button"].unbind(BTN_CLICK)
            tile['state'] = 1
            queue.append(tile["x_y"])

    # Get neighbouring blocks
    def getNeighbours(self, x, y):
        neighbours = []
        coords = [
            # {"x": x-1,  "y": y-1},  #top right
            {"x": x-1,  "y": y},    #top middle
            # {"x": x-1,  "y": y+1},  #top left
            {"x": x,    "y": y-1},  #left
            {"x": x,    "y": y+1},  #right
            # {"x": x+1,  "y": y-1},  #bottom right
            {"x": x+1,  "y": y},    #bottom middle
            # {"x": x+1,  "y": y+1},  #bottom left
        ]
        for n in coords:
            try:
                neighbours.append(self.game_seed[n["x"]][n["y"]])
            except KeyError:
                pass
        return neighbours


# def main():
#     # Create TK instance
#     window = Tk()
#     # Set program title
#     window.title("Quantum Minesweeper")
#     # create game instance
#     minesweeper = Minesweeper(window)
#     # run event loop
#     window.mainloop()

# if __name__ == '__main__':
#     main()