import TextUI as tui
import BombTester as bt
import numpy as np

def main():
    # Takes in input from user
    GRID_SIZE = int(input('Please enter a size: '))
    # Initialize the board and make a copy of it, solution board and play board
    revealed = initialize(GRID_SIZE)
    grid = np.copy(revealed)

    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y][0] == '1':
                grid[x][y] = '*'
            else:
                grid[x][y] = '-'

    tui.draw(revealed)
    play(grid, revealed)

# Populate the board with bomb_tester results
def initialize(grid_size):
    # Set the board size
    bomb_grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    
    for x in range(grid_size):
        for y in range(grid_size):
            bomb_grid[x][y] = bt.get_count(6)[0] # Returns a string of qubits
    return bomb_grid

# Game logic
def play(grid, solution):
    while True:
        tui.draw(grid)
        try:
            # Prompt user to select a block
            x, y = map(int, input('Select a block to test (x y): ').split())
            if (x >= len(grid) or y >= len(grid)):
                raise Exception()
            # Check the detector qubit in the string
            if (solution[x][y][1] == '1'):
                print('Bomb tester says there is no bomb')
            else:
                print('Bomb tester says there is a bomb')
            # Prompt user to predict whether if there's a bomb or not
            selection = input('Input 1 if you think there is a bomb, otherwise 0: ')

            # Continue the game if user picks right, otherwise exit
            if solution[x][y][0] == selection:
                print('Congratz, you predicted correctly')
                grid[x][y] = '◻'
            else:
                print('You lose')
                break;

        except:
            print('Invalid input.')
            break

if __name__ == '__main__':
    main()