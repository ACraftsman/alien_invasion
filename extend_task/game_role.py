import pygame
import sys
def run_code():
    pygame.init()
    screen = pygame.display.set_mode((1200,700))
    pygame.display.set_caption("Game Role")
    image = pygame.image.load('images/badass.bmp')
    image = pygame.transform.scale(image, (1200, 700))
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    rect.center = screen_rect.center
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill((0,0,0))
        screen.blit(image, rect)
        pygame.display.flip()

if __name__ == "__main__":
    run_code()