import pygame

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
WHITE = (255, 255, 255)


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
            print(event)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game_loop()
