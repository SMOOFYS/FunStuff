import pygame
import random
import math
import sys

pygame.init()

# --- Config ---
WIDTH, HEIGHT = 900, 550
FPS = 60
GRAVITY = 0.6
JUMP_FORCE = -13
PLAYER_SPEED = 5
OBSTACLE_SPEED_START = 5
SPEED_INCREMENT = 0.002

# --- Neon Colors ---
BLACK       = (5, 5, 15)
NEON_CYAN   = (0, 255, 230)
NEON_PINK   = (255, 0, 180)
NEON_YELLOW = (255, 230, 0)
NEON_GREEN  = (0, 255, 100)
NEON_PURPLE = (180, 0, 255)
WHITE       = (255, 255, 255)
GRID_COLOR  = (20, 20, 50)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GRAVITY FLIP — Neon Runner")
clock = pygame.time.Clock()

font_big   = pygame.font.SysFont("Courier New", 64, bold=True)
font_med   = pygame.font.SysFont("Courier New", 32, bold=True)
font_small = pygame.font.SysFont("Courier New", 22)

# --- Utility ---
def neon_rect(surface, color, rect, width=2, glow=8):
    for i in range(glow, 0, -2):
        alpha = max(30, 80 - i * 8)
        glow_surf = pygame.Surface((rect[2] + i*2, rect[3] + i*2), pygame.SRCALPHA)
        pygame.draw.rect(glow_surf, (*color, alpha), (0, 0, rect[2]+i*2, rect[3]+i*2), border_radius=4)
        surface.blit(glow_surf, (rect[0]-i, rect[1]-i))
    pygame.draw.rect(surface, color, rect, width, border_radius=4)

def neon_line(surface, color, p1, p2, width=2, glow=6):
    for i in range(glow, 0, -2):
        alpha = max(20, 60 - i * 8)
        s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pygame.draw.line(s, (*color, alpha), p1, p2, width + i*2)
        surface.blit(s, (0, 0))
    pygame.draw.line(surface, color, p1, p2, width)

def neon_text(surface, text, font, color, x, y, center=True):
    for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
        glow = font.render(text, True, tuple(min(255, c+80) for c in color))
        r = glow.get_rect()
        if center: r.center = (x+dx, y+dy)
        else: r.topleft = (x+dx, y+dy)
        gs = pygame.Surface(glow.get_size(), pygame.SRCALPHA)
        gs.fill((0,0,0,0))
        gs.blit(glow, (0,0))
        gs.set_alpha(60)
        surface.blit(gs, r)
    txt = font.render(text, True, color)
    r = txt.get_rect()
    if center: r.center = (x, y)
    else: r.topleft = (x, y)
    surface.blit(txt, r)

# --- Stars/Particles ---
class Star:
    def __init__(self):
        self.reset()
    def reset(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.speed = random.uniform(0.5, 2.5)
        self.size = random.randint(1, 3)
        self.color = random.choice([NEON_CYAN, NEON_PINK, NEON_PURPLE, WHITE])
    def update(self, game_speed):
        self.x -= self.speed * (game_speed / OBSTACLE_SPEED_START)
        if self.x < 0:
            self.x = WIDTH
            self.y = random.randint(0, HEIGHT)
    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.size)

class Particle:
    def __init__(self, x, y, color):
        self.x, self.y = x, y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-4, 1)
        self.life = random.randint(15, 35)
        self.max_life = self.life
        self.color = color
        self.size = random.randint(2, 5)
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15
        self.life -= 1
    def draw(self, surf):
        if self.life <= 0: return
        alpha = int(255 * self.life / self.max_life)
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (self.size, self.size), self.size)
        surf.blit(s, (int(self.x)-self.size, int(self.y)-self.size))

# --- Player ---
class Player:
    W, H = 34, 34
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = 130
        self.y = HEIGHT - 80 - self.H
        self.vy = 0
        self.gravity_dir = 1  # 1 = down, -1 = up
        self.on_ground = False
        self.alive = True
        self.flip_cooldown = 0
        self.trail = []
        self.color = NEON_CYAN
        self.rotation = 0
        self.spin = 0

    def flip_gravity(self):
        if self.flip_cooldown <= 0:
            self.gravity_dir *= -1
            self.vy = JUMP_FORCE * self.gravity_dir * -1
            self.flip_cooldown = 12
            self.spin = 18 * self.gravity_dir
            return True
        return False

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, self.W, self.H)

    def update(self, particles):
        self.vy += GRAVITY * self.gravity_dir
        self.vy = max(-18, min(18, self.vy))
        self.y += self.vy
        self.flip_cooldown = max(0, self.flip_cooldown - 1)

        # Ground/ceiling collision
        floor_y = HEIGHT - 80 - self.H
        ceil_y  = 80

        if self.gravity_dir == 1 and self.y >= floor_y:
            self.y = floor_y
            self.vy = 0
            self.on_ground = True
        elif self.gravity_dir == -1 and self.y <= ceil_y:
            self.y = ceil_y
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # Spin effect
        if abs(self.spin) > 0:
            self.rotation += self.spin
            self.spin *= 0.85
            if abs(self.spin) < 0.5: self.spin = 0

        # Trail
        self.trail.append((self.x + self.W//2, self.y + self.H//2))
        if len(self.trail) > 14:
            self.trail.pop(0)

        # Ambient particles
        if random.random() < 0.15:
            particles.append(Particle(self.x + self.W//2, self.y + self.H//2, self.color))

    def draw(self, surf):
        # Trail
        for i, (tx, ty) in enumerate(self.trail):
            alpha = int(160 * i / len(self.trail))
            size = max(2, int(8 * i / len(self.trail)))
            s = pygame.Surface((size*2+4, size*2+4), pygame.SRCALPHA)
            pygame.draw.circle(s, (*self.color, alpha), (size+2, size+2), size)
            surf.blit(s, (tx-size-2, ty-size-2))

        # Body (rotated square)
        body_surf = pygame.Surface((self.W, self.H), pygame.SRCALPHA)
        # Inner fill
        pygame.draw.rect(body_surf, (*NEON_CYAN, 60), (0,0,self.W,self.H), border_radius=6)
        pygame.draw.rect(body_surf, NEON_CYAN, (0,0,self.W,self.H), 3, border_radius=6)
        # Cross detail
        pygame.draw.line(body_surf, (*NEON_PINK, 180), (self.W//2,4), (self.W//2, self.H-4), 2)
        pygame.draw.line(body_surf, (*NEON_PINK, 180), (4, self.H//2), (self.W-4, self.H//2), 2)

        rotated = pygame.transform.rotate(body_surf, self.rotation)
        r = rotated.get_rect(center=(self.x+self.W//2, self.y+self.H//2))
        surf.blit(rotated, r)

# --- Obstacles ---
class Obstacle:
    TYPES = ['wall', 'spike_floor', 'spike_ceil', 'double', 'moving']

    def __init__(self, speed):
        self.speed = speed
        self.alive = True
        self.type = random.choice(self.TYPES)
        self.color = random.choice([NEON_PINK, NEON_YELLOW, NEON_PURPLE])
        self._setup()

    def _setup(self):
        floor_y = HEIGHT - 80
        ceil_y  = 80
        mid = (floor_y + ceil_y) // 2

        if self.type == 'wall':
            gap = random.randint(110, 160)
            gap_y = random.randint(ceil_y + 20, floor_y - gap - 20)
            self.rects = [
                pygame.Rect(WIDTH + 20, ceil_y, 30, gap_y - ceil_y),
                pygame.Rect(WIDTH + 20, gap_y + gap, 30, floor_y - gap_y - gap),
            ]
        elif self.type == 'spike_floor':
            self.rects = [pygame.Rect(WIDTH + 20, floor_y - 30, 28, 30)]
        elif self.type == 'spike_ceil':
            self.rects = [pygame.Rect(WIDTH + 20, ceil_y, 28, 30)]
        elif self.type == 'double':
            self.rects = [
                pygame.Rect(WIDTH + 20, floor_y - 28, 24, 28),
                pygame.Rect(WIDTH + 20, ceil_y, 24, 28),
            ]
        elif self.type == 'moving':
            self.rects = [pygame.Rect(WIDTH + 20, mid - 15, 24, 30)]
            self.move_dir = 1
            self.move_speed = random.uniform(1.5, 3.0)

    def update(self):
        for r in self.rects:
            r.x -= self.speed
        if self.type == 'moving':
            floor_y = HEIGHT - 80
            ceil_y = 80
            for r in self.rects:
                r.y += self.move_speed * self.move_dir
            if self.rects[0].bottom >= floor_y or self.rects[0].top <= ceil_y:
                self.move_dir *= -1
        if self.rects[0].right < -40:
            self.alive = False

    def draw(self, surf):
        for r in self.rects:
            if self.type in ('spike_floor', 'spike_ceil', 'double'):
                # Draw diamond/spike shape
                cx, cy = r.centerx, r.centery
                pts = [(cx, r.top - 10), (r.right + 10, cy), (cx, r.bottom + 10), (r.left - 10, cy)]
                for i in range(6, 0, -2):
                    alpha = max(20, 60 - i*8)
                    s = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
                    pygame.draw.polygon(s, (*self.color, alpha), pts)
                    surf.blit(s, (0, 0))
                pygame.draw.polygon(surf, self.color, pts)
                pygame.draw.polygon(surf, WHITE, pts, 2)
            else:
                neon_rect(surf, self.color, (r.x, r.y, r.w, r.h), width=3, glow=10)
                # Fill
                inner = pygame.Surface((r.w, r.h), pygame.SRCALPHA)
                inner.fill((*self.color, 40))
                surf.blit(inner, (r.x, r.y))

    def collides(self, player_rect):
        # Slightly shrunk hitbox for fairness
        shrunk = player_rect.inflate(-8, -8)
        return any(r.colliderect(shrunk) for r in self.rects)

# --- Draw background ---
def draw_background(surf, scroll, game_speed):
    surf.fill(BLACK)
    # Scrolling grid
    grid_step = 60
    offset = int(scroll) % grid_step
    for x in range(-grid_step, WIDTH + grid_step, grid_step):
        pygame.draw.line(surf, GRID_COLOR, (x - offset, 0), (x - offset, HEIGHT), 1)
    for y in range(0, HEIGHT, grid_step):
        pygame.draw.line(surf, GRID_COLOR, (0, y), (WIDTH, y), 1)

    # Floor and ceiling
    floor_y = HEIGHT - 80
    ceil_y  = 80
    neon_line(surf, NEON_CYAN, (0, floor_y), (WIDTH, floor_y), 3, glow=10)
    neon_line(surf, NEON_CYAN, (0, ceil_y),  (WIDTH, ceil_y),  3, glow=10)
    # Zone fill
    floor_surf = pygame.Surface((WIDTH, HEIGHT - floor_y), pygame.SRCALPHA)
    floor_surf.fill((*NEON_CYAN, 18))
    surf.blit(floor_surf, (0, floor_y))
    ceil_surf = pygame.Surface((WIDTH, ceil_y), pygame.SRCALPHA)
    ceil_surf.fill((*NEON_CYAN, 18))
    surf.blit(ceil_surf, (0, 0))

# --- HUD ---
def draw_hud(surf, score, best, game_speed, grav_dir):
    neon_text(surf, f"SCORE  {score:06d}", font_small, NEON_YELLOW, 20, 22, center=False)
    neon_text(surf, f"BEST   {best:06d}", font_small, NEON_PINK, 20, 46, center=False)
    speed_str = f"SPD {game_speed:.1f}"
    neon_text(surf, speed_str, font_small, NEON_GREEN, WIDTH - 160, 22, center=False)
    arrow = "▲ FLIP UP" if grav_dir == 1 else "▼ FLIP DOWN"
    neon_text(surf, arrow, font_small, NEON_CYAN, WIDTH//2, 42, center=True)

# --- Screens ---
def draw_title(surf, best):
    draw_background(surf, 0, OBSTACLE_SPEED_START)
    neon_text(surf, "GRAVITY", font_big, NEON_CYAN, WIDTH//2, HEIGHT//2 - 80)
    neon_text(surf, "FLIP", font_big, NEON_PINK, WIDTH//2, HEIGHT//2 - 10)
    neon_text(surf, "PRESS  SPACE  OR  ↑  TO  PLAY", font_small, WHITE, WIDTH//2, HEIGHT//2 + 70)
    neon_text(surf, "SPACE / ↑ / W  =  FLIP GRAVITY", font_small, NEON_YELLOW, WIDTH//2, HEIGHT//2 + 105)
    if best > 0:
        neon_text(surf, f"BEST: {best:06d}", font_med, NEON_GREEN, WIDTH//2, HEIGHT//2 + 150)

def draw_game_over(surf, score, best):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 10, 170))
    surf.blit(overlay, (0, 0))
    neon_text(surf, "GAME OVER", font_big, NEON_PINK, WIDTH//2, HEIGHT//2 - 70)
    neon_text(surf, f"SCORE  {score:06d}", font_med, NEON_YELLOW, WIDTH//2, HEIGHT//2 + 10)
    neon_text(surf, f"BEST   {best:06d}", font_med, NEON_CYAN, WIDTH//2, HEIGHT//2 + 55)
    neon_text(surf, "SPACE to retry  •  ESC to quit", font_small, WHITE, WIDTH//2, HEIGHT//2 + 115)

# --- Main ---
def main():
    state = "title"
    best = 0
    player = Player()
    obstacles = []
    particles = []
    stars = [Star() for _ in range(80)]
    score = 0
    game_speed = OBSTACLE_SPEED_START
    scroll = 0
    spawn_timer = 0
    spawn_interval = 90

    while True:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
                if state == "title":
                    if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                        # Start game
                        state = "playing"
                        player.reset()
                        obstacles.clear()
                        particles.clear()
                        score = 0
                        game_speed = OBSTACLE_SPEED_START
                        spawn_timer = 0
                elif state == "playing":
                    if event.key in (pygame.K_SPACE, pygame.K_UP, pygame.K_w):
                        if player.flip_gravity():
                            for _ in range(12):
                                particles.append(Particle(player.x+player.W//2, player.y+player.H//2, NEON_CYAN))
                elif state == "gameover":
                    if event.key == pygame.K_SPACE:
                        state = "playing"
                        player.reset()
                        obstacles.clear()
                        particles.clear()
                        score = 0
                        game_speed = OBSTACLE_SPEED_START
                        spawn_timer = 0

        if state == "playing":
            scroll += game_speed
            game_speed += SPEED_INCREMENT
            score += 1
            if score > best: best = score

            player.update(particles)

            # Spawn obstacles
            spawn_timer += 1
            if spawn_timer >= spawn_interval:
                obstacles.append(Obstacle(game_speed))
                spawn_timer = 0
                spawn_interval = max(45, int(90 - score/600))

            for obs in obstacles:
                obs.speed = game_speed
                obs.update()
                if obs.collides(player.rect):
                    player.alive = False
                    for _ in range(30):
                        particles.append(Particle(player.x+player.W//2, player.y+player.H//2, NEON_PINK))
                    for _ in range(20):
                        particles.append(Particle(player.x+player.W//2, player.y+player.H//2, NEON_YELLOW))

            obstacles = [o for o in obstacles if o.alive]
            particles = [p for p in particles if p.life > 0]
            for p in particles: p.update()
            for s in stars: s.update(game_speed)

            if not player.alive:
                state = "gameover"

        # --- Draw ---
        draw_background(screen, scroll, game_speed)
        for s in stars: s.draw(screen)
        for p in particles: p.draw(screen)

        if state == "title":
            draw_title(screen, best)

        elif state == "playing":
            for obs in obstacles: obs.draw(screen)
            player.draw(screen)
            draw_hud(screen, score, best, game_speed, player.gravity_dir)

        elif state == "gameover":
            for obs in obstacles: obs.draw(screen)
            for p in particles: p.draw(screen)
            draw_game_over(screen, score, best)

        pygame.display.flip()

if __name__ == "__main__":
    main()