import pygame
from settings import TILE, COLS, ROWS, BLUE, WHITE, WALL, PELLET, EMPTY

# 1=wall, 0=pellet, 9=empty floor
# row 0 is the top, each number is one 32x32 tile.
GRID = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,9,0,1,1,0,9,1,1,0,1,1,1,1],
    [1,1,1,1,0,1,9,9,9,9,9,9,9,9,1,0,1,1,1,1],
    [1,1,1,1,0,1,9,1,9,9,9,9,1,9,1,0,1,1,1,1],
    [9,9,9,9,0,9,9,1,9,9,9,9,1,9,9,0,9,9,9,9],
    [1,1,1,1,0,1,9,1,1,1,1,1,1,9,1,0,1,1,1,1],
    [1,1,1,1,0,1,9,9,9,9,9,9,9,9,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


class Maze:
    def __init__(self):
        # Copy grd to modify (eating pellets changes 0 → 9)
        self.grid = [row[:] for row in GRID]

    def is_wall(self, x, y):
        # Conv pxl pos to grd col/row w/int div
        col, row = int(x // TILE), int(y // TILE)
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.grid[row][col] == WALL
        return True  # Out of bounds counts as a wall

    def eat_pellet(self, x, y):
        # If on pellet remove it and return 10 points
        col, row = int(x // TILE), int(y // TILE)
        if 0 <= row < ROWS and 0 <= col < COLS and self.grid[row][col] == PELLET:
            self.grid[row][col] = EMPTY
            return 10
        return 0

    def has_pellets(self):
        # Win condition -> False when every pellet is eaten
        return any(PELLET in row for row in self.grid)

    def draw(self, surface):
        for r in range(ROWS):
            for c in range(COLS):
                x, y = c * TILE, r * TILE
                if self.grid[r][c] == WALL:
                    pygame.draw.rect(surface, BLUE, (x+1, y+1, TILE-2, TILE-2), border_radius=4)
                elif self.grid[r][c] == PELLET:
                    pygame.draw.circle(surface, WHITE, (x + TILE//2, y + TILE//2), 4)