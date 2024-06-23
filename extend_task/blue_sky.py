import sys
import pygame


def run_code():
    pygame.init()
    width = 700
    height = 500
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Blue Sky")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        bg_color = (0, 0, 255)
        screen.fill(bg_color)
        pygame.display.flip()


if __name__ == "__main__":
    run_code()
