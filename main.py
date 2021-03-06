import pygame 
import random 

WIDTH = 800 
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("AI SEARCH STUDY")
pygame.init()



# ADDING COLORS

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)



class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row 
        self.col = col
        self.x = col * width
        self.y = row * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))



def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            sp = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    grid[0][0].color = BLACK
    # to be cont


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))




def main(win, width):
    ROWS = 50 
    grid = make_grid(ROWS, width)


    run = True
    found = False


    while run:



