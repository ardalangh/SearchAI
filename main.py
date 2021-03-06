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


