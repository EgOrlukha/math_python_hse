import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_rectangle(display, x, y, w, h, color):
    pygame.draw.rect(display, color, [x, y, w, h])


def game_loop():
    pygame.init()
    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Simple pygame program')
    gameDisplay.fill(WHITE)

    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pygame.draw.rect(gameDisplay, BLACK, [50, 50, 100, 100])
        pygame.draw.line(gameDisplay, RED, (0, 0), (800, 600), 2)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game_loop()
