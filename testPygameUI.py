import pygame, sys
import pygame_menu
from typing import Tuple, Any

SIZE = [4]

icon = pygame.image.load('images/mineClicked.png')

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption('Quantum Minesweeper')
pygame.display.set_icon(icon)

# Set difficulty and return size to set the board
def set_difficulty(value:Tuple, difficulty: int)-> None:
    selected, index = value
    print(f'Selected difficulty: "{selected}" with size ({difficulty}) at index {index}')
    SIZE[0]=difficulty

def start_the_game()-> None:
    print(f'Game size selected: {SIZE[0]} x {SIZE[0]}') # Get difficulty selected (Call SIZE[0] to get size)
    
    screen = pygame.display.set_mode((700,700))
    screen.fill((255,255,255))
    pygame.display.flip()
        
    # initialize board with bomb grid
    # draw grid?

    pass

def main_menu():
    menu = pygame_menu.Menu(
        height = 700,
        title='Quantum Minesweeper',
        width=700,
        theme=pygame_menu.themes.THEME_GREEN
    )

    menu.add.selector('Difficulty : ', [('Easy',4), ('Medium', 6), ('Hard', 8)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


if __name__ == '__main__':
    main_menu()
