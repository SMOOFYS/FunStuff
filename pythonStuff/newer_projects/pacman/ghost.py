import pygame, random, math
from settings import TILE, WHITE, BLACK, GHOST_SPEED

DIRS = [(1,0),(-1,0),(0,1),(0,-1)]


class Ghost:
    def __init__(self, col, row, color):
        self.x = col * TILE + TILE // 2
        self.y = row * TILE + TILE // 2
        self.color = color
        self.r = 13
        self.dx, self.dy = random.choice(DIRS)

    def _can_move(self, maze, x, y):
        m = self.r - 2
        return not any(maze.is_wall(x+ox, y+oy) for ox, oy in [(-m,-m),(m,-m),(-m,m),(m,m)])

    def update(self, maze):
        nx, ny = self.x + self.dx * GHOST_SPEED, self.y + self.dy * GHOST_SPEED
        if not self._can_move(maze, nx, ny):
            # if u hit a wall just pick a rand direction
            options = DIRS[:]
            random.shuffle(options)
            for dx, dy in options:
                tx, ty = self.x + dx * GHOST_SPEED, self.y + dy * GHOST_SPEED
                if self._can_move(maze, tx, ty):
                    self.dx, self.dy = dx, dy
                    self.x, self.y = tx, ty
                    return
        else:
            self.x, self.y = nx, ny

    def touches_pacman(self, px, py):
        # Simple circle-circle collision: overlapping if distance < sum of radii
        return math.hypot(self.x - px, self.y - py) < (self.r + 13)

    def draw(self, surface):
        x, y, r = int(self.x), int(self.y), self.r
        pygame.draw.circle(surface, self.color, (x, y - 2), r)         # head
        pygame.draw.rect(surface, self.color, (x-r, y-2, r*2, r))      # body
        for i in range(3):                                               # skirt bumps
            pygame.draw.circle(surface, BLACK, (x - r + 4 + i*9, y+r), 4)
        for ox in (-5, 5):                                               # eyes
            pygame.draw.circle(surface, WHITE, (x+ox, y-4), 4)
            pygame.draw.circle(surface, BLACK, (x+ox+1, y-3), 2)