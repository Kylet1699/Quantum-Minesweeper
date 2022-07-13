import math
import random
from BombTester import *

GRID_SIZE = 6

grid = [[-1 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]
bomb_grid = [[0 for x in range(GRID_SIZE)] for y in range(GRID_SIZE)]

# Initialize the grid with bombs
def initialize():
    # i = GRID_SIZE ** 2 / 4 # Modify this to change number of bombs on the grid
    # while i > 0:
    #     x = random.randint(0, GRID_SIZE - 1)
    #     y = random.randint(0, GRID_SIZE - 1)
    #     if bomb_grid[x][y] == 0:
    #         bomb_grid[x][y] = 1
    #         i -= 1
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            bomb_grid[x][y] = get_count(6)


# Draw the user view of the game state
def draw(hidden):
    print('\n')
    # Draw the top border
    print('\t┌', end='')
    for i in range(0, GRID_SIZE):
        print('─' * 11, end='')
        if i != GRID_SIZE - 1:
            print('┬', end='')
    print('┐', sep='')
    for i in range(0, GRID_SIZE):
        # Draw the lines between each row
        if i != 0:
            print('\t├', end='')
            for k in range(0, GRID_SIZE):
                print('─' * 11, end='')
                if k != GRID_SIZE - 1:
                    print('┼', end='')
            print('┤', sep='')
        # Draw the row
        for j in range(0, GRID_SIZE):
            if j == 0:
                print('\t│', end='')
            # if grid[i][j] == 1:
            #     print(' ⚑ ', end='│')
            # elif grid[i][j] == 0:
            #     print(' * ', end='│')
            elif (hidden == False):
                print(bomb_grid[i][j], end='│')
            elif (hidden == True):
                print('           ', end='│')
            if (j == GRID_SIZE - 1 ):
                if (hidden == False):
                    print(bomb_grid[i][j])
                if (hidden == True):
                    print('           ')
    # Draw the bottom border
    print('\t└', end='')
    for i in range(0, GRID_SIZE):
        print('─' * 11, end='')
        if i != GRID_SIZE - 1:
            print('┴', end='')
    print('┘', sep='')
    print('\n')


# Update the game with the new block
def update(x, y, option):
    if bomb_grid[x][y] == 1 and not option == 1 :
        return False

    grid[x][y] = option

    return True


# Start the game
def play():
    while True:
        try:
            # Prompt user to select a block
            x, y = map(int , input('Select a block to test (x y): ').split())
            if x >= GRID_SIZE or x < 0 or y >= GRID_SIZE or y < 0:
                raise Exception()
            # Prompt user to choose action
            selection = input('Select an option (C = check, F = flag): ')
            option = -1

            if selection == ('C' or 'c'):
                option = 0
            elif selection == ('F' or 'f'):
                option = 1
            else:
                raise Exception()

            # Update the game with the selected options
            if update(x, y, option):
                draw()
            else:
                print('\nGAME OVER\n')
                break
        except:
            print('Invalid input.')
            break

initialize()
draw(False)
draw(True)
play()

