# All constants in one place. Change values here to affect the whole game.

TILE  = 32
COLS  = 20
ROWS  = 15
W     = COLS * TILE 
H     = ROWS * TILE + 40  # +40 4 da score bar
FPS   = 60

# Colors (R, G, B)
BLACK  = (0,   0,   0)
WHITE  = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE   = (0,   0,   200)
RED    = (220, 0,   0)
PINK   = (255, 180, 255)

# Speeds in pixels per frame
PAC_SPEED   = 3
GHOST_SPEED = 2

# Tile types in mze grd
WALL   = 1
PELLET = 0
EMPTY  = 9