import BombTester as bt

def draw(grid):
    for x in range(len(grid)):
        for y in range(len(grid)):
            print(grid[x][y], end = "      ")
        print("\n")
        