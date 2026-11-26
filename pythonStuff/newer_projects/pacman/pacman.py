import pygame, math
from settings import TILE, YELLOW, BLACK, PAC_SPEED


class Pacman:
    def __init__(self, col, row):
        self.x = col * TILE + TILE // 2
        self.y = row * TILE + TILE // 2
        self.r = 13
        self.dx, self.dy   = 0, 0  # curr dir (unit: -1, 0, or 1)
        self.ndx, self.ndy = 0, 0  # buffered dir from last key press
        self.mouth, self.mdir = 0, 1

    def set_direction(self, dx, dy):
        self.ndx, self.ndy = dx, dy

    def _blocked(self, maze, x, y):
        m = self.r - 2
        return any(maze.is_wall(x+ox, y+oy) for ox, oy in [(-m,-m),(m,-m),(-m,m),(m,m)])

    def update(self, maze):
        # Try buffered dir -> if clear, switch to it
        nx = self.x + self.ndx * PAC_SPEED
        ny = self.y + self.ndy * PAC_SPEED
        if not self._blocked(maze, nx, ny):
            self.dx, self.dy = self.ndx, self.ndy

        # Move in curr dir if not blocked
        nx = self.x + self.dx * PAC_SPEED
        ny = self.y + self.dy * PAC_SPEED
        if not self._blocked(maze, nx, ny):
            self.x, self.y = nx, ny

        # Screen wrap
        self.x %= TILE * 20

        # Mouth anim
        self.mouth += 3 * self.mdir
        if self.mouth >= 35 or self.mouth <= 0:
            self.mdir *= -1

    def draw(self, surface):
        pygame.draw.circle(surface, YELLOW, (int(self.x), int(self.y)), self.r)
        if self.mouth > 0:
            facing = math.atan2(self.dy, self.dx) if (self.dx or self.dy) else 0
            a = math.radians(self.mouth)
            pts = [
                (int(self.x), int(self.y)),
                (int(self.x + (self.r+2) * math.cos(facing - a)), int(self.y + (self.r+2) * math.sin(facing - a))),
                (int(self.x + (self.r+2) * math.cos(facing + a)), int(self.y + (self.r+2) * math.sin(facing + a))),
            ]
            pygame.draw.polygon(surface, BLACK, pts)