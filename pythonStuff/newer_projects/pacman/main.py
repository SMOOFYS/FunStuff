import pygame
from settings import W, H, TILE, ROWS, FPS, BLACK, WHITE, YELLOW, RED, PINK
from maze   import Maze
from pacman import Pacman
from ghost  import Ghost


def make_actors():
    # Spawn Pac-Man and both ghosts at their starting positions
    pac    = Pacman(col=1, row=1)
    ghosts = [Ghost(9, 7, RED), Ghost(10, 7, PINK)]
    return pac, ghosts


def main():
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Pac-Man")
    clock    = pygame.time.Clock()
    font     = pygame.font.SysFont(None, 28)
    font_big = pygame.font.SysFont(None, 56)

    maze  = Maze()
    score = 0
    lives = 3
    pac, ghosts = make_actors()
    state = "playing"   # states: "playing", "paused", "game_over", "you_win"
    pause_timer = 0     # counts down frames after losing a life

    running = True
    while running:
        clock.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if state == "playing":
                    if event.key in (pygame.K_LEFT,  pygame.K_a): pac.set_direction(-1,  0)
                    if event.key in (pygame.K_RIGHT, pygame.K_d): pac.set_direction( 1,  0)
                    if event.key in (pygame.K_UP,    pygame.K_w): pac.set_direction( 0, -1)
                    if event.key in (pygame.K_DOWN,  pygame.K_s): pac.set_direction( 0,  1)
                if state in ("game_over", "you_win") and event.key == pygame.K_SPACE:
                    maze, score, lives = Maze(), 0, 3
                    pac, ghosts = make_actors()
                    state = "playing"

        # Update
        if state == "playing":
            pac.update(maze)
            for g in ghosts: g.update(maze)

            score += maze.eat_pellet(pac.x, pac.y)  # eat pellet at Pac-Man's position

            if any(g.touches_pacman(pac.x, pac.y) for g in ghosts):
                lives -= 1
                state = "game_over" if lives <= 0 else "paused"
                pause_timer = 90  # ~1.5 seconds at 60fps

            if not maze.has_pellets():
                state = "you_win"

        elif state == "paused":
            pause_timer -= 1
            if pause_timer <= 0:
                pac, ghosts = make_actors()  # respawn, keep score and maze
                state = "playing"

        # --- Draw ---
        screen.fill(BLACK)
        maze.draw(screen)
        pac.draw(screen)
        for g in ghosts: g.draw(screen)

        # Score bar
        screen.blit(font.render(f"Score: {score}", True, WHITE),  (10, ROWS*TILE+10))
        screen.blit(font.render(f"Lives: {lives}", True, YELLOW), (W-120, ROWS*TILE+10))

        # Overlay messages
        if state == "game_over":
            msg = font_big.render(f"GAME OVER  {score}pts", True, YELLOW)
            screen.blit(msg, (W//2 - msg.get_width()//2, H//2 - 40))
            hint = font.render("SPACE to restart", True, WHITE)
            screen.blit(hint, (W//2 - hint.get_width()//2, H//2 + 20))
        elif state == "you_win":
            msg = font_big.render(f"YOU WIN!  {score}pts", True, YELLOW)
            screen.blit(msg, (W//2 - msg.get_width()//2, H//2 - 40))
            hint = font.render("SPACE to restart", True, WHITE)
            screen.blit(hint, (W//2 - hint.get_width()//2, H//2 + 20))

        pygame.display.flip()  # push everything drawn this frame to the screen

    pygame.quit()


if __name__ == "__main__":
    main()