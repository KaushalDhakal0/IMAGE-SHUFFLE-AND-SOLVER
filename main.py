import sys
import random
import pygame
from functions import shift,newshift,AIshift,shuffle,convertToArray,goalState,determineChild
from astar import Astar
IMAGE_FILE = "girl.jpg"
IMAGE_SIZE = (800, 600)
TILE_WIDTH = int(800 / 3)
TILE_HEIGHT = int(600 / 3)
COLUMNS = 3
ROWS = 3
frontier = []
explored = []
index = []
EMPTY_TILE = (COLUMNS - 1, ROWS - 1)
BLACK = (0, 0, 0)
hor_border = pygame.Surface((TILE_WIDTH, 1))
hor_border.fill(BLACK)
ver_border = pygame.Surface((1, TILE_HEIGHT))
ver_border.fill(BLACK)

image = pygame.image.load(IMAGE_FILE)
tiles = {}
for c in range(COLUMNS):
    for r in range(ROWS):
        tile = image.subsurface(c * TILE_WIDTH, r * TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT)
        tiles[(c, r)] = (tile)
        if (c, r) != EMPTY_TILE:
            tile.blit(hor_border, (0, 0))
            tile.blit(hor_border, (0, TILE_HEIGHT - 1))
            tile.blit(ver_border, (0, 0))
            tile.blit(ver_border, (TILE_WIDTH - 1, 0))
            tile.set_at((1, 1), BLACK)
            tile.set_at((1, TILE_HEIGHT - 2), BLACK)
            tile.set_at((TILE_WIDTH - 2, 1), BLACK)
            tile.set_at((TILE_WIDTH - 2, TILE_HEIGHT - 2), BLACK)
tiles[EMPTY_TILE].fill(BLACK)
state = {(col, row): (col, row)
         for col in range(COLUMNS) for row in range(ROWS)}
GOALSTATE = tiles.copy()
(emptyc, emptyr) = EMPTY_TILE
pygame.init()
display = pygame.display.set_mode(IMAGE_SIZE)
pygame.display.set_caption("Image suffle and solve")
display.blit(image, (0, 0))
pygame.display.flip()

at_start = True
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if at_start:
            shuffle()
            at_start = False
        else:
            Astar(convertToArray())
            AIshift()