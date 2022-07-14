import TextUI as tui
import BombTester as bt
import numpy as np

def main():
    # Takes in input from user
    size = 4
    try:
        difficulty = input('Select difficulty (E = easy, M = medium, H = hard): ')
        if difficulty in ['e', 'E']:
            size = 4
        elif difficulty in ['m', 'M']:
            size = 6
        elif difficulty in ['h', 'H']:
            size = 8
        else:
            raise 
    except:
        print('Invalid input, defaulting to easy')
    
    # Initialize the board and make a copy of it, solution board and play board
    revealed = initialize(size)
    grid = np.copy(revealed)

    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y][0] == '1':
                grid[x][y] = '*'
            else:
                grid[x][y] = '-'

    tui.draw(revealed)
    play(grid, revealed, size)

# Populate the board with bomb_tester results
def initialize(grid_size):
    # Set the board size
    bomb_grid = [[0 for x in range(grid_size)] for y in range(grid_size)]
    
    for x in range(grid_size):
        for y in range(grid_size):
            bomb_grid[x][y] = bt.get_count(6)[0] # Returns a string of qubits
    return bomb_grid

# Count the number of neighbouring bombs (detector qubit)
def get_neighbours(x, y, size, solution):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i >= 0 and j >= 0 and i < size and j < size
                and solution[i][j][1] == '1' and not (x == i and y == j)):
                count += 1

    return count

# Clear all neighbouring blocks recursively that do not touch a bomb (detector qubit)
def clear_neighbours(x, y, size, grid, solution):        
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i >= 0 and j >= 0 and i < size and j < size and
                get_neighbours(i, j, size, solution) == 0 and
                # If the block has no dectected bombs, clear it and check the surrounding blocks
                grid[i][j] in ['*', '-']):
                grid[i][j] = 0
                clear_neighbours(i, j, size, grid, solution)
                
# Game logic
def play(grid, solution, size):
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
                grid[x][y] = get_neighbours(x, y, size, solution)
                solution[x][y] = '0000000'
                clear_neighbours(x, y, size, grid, solution)
            else:
                print('You lose')
                break

        except Exception as e:
            print('Error:', e)
            break

if __name__ == '__main__':
    main()