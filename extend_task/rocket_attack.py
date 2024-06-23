import sys
import pygame
from pygame.sprite import Sprite,Group

def main():
    pygame.init()
    pygame.key.set_repeat(10, 15)
    screen = pygame.display.set_mode((700, 500))
    pygame.display.set_caption("Rocket Attack Demo")
    screen_rect = screen.get_rect()
    rocket = create_rocket(screen_rect)
    # rocket_rect = rocket.get_rect()
    rocket.get_rect().y = screen_rect.centery
    # bullets = Group()
    while True:
        # updateScreen(screen, rocket)

        screen.fill((255, 255, 255))
        move_rocket(rocket.get_rect(), screen.get_rect())
        screen.blit(rocket, rocket.get_rect())
        pygame.display.flip()
class bullet(Sprite):
    def __init__(self, width, speed):
        # 子弹宽度
        self.width = width
        # 子弹速度
        self.speed = speed

    def aa(self):
        pass

        

def create_rocket(screen_rect):
    rocket = pygame.image.load("images/rocket.jpg")
    rocket = pygame.transform.scale(rocket, (50, 80))
    rocket = pygame.transform.rotate(rocket, -90)
    rocket_rect = rocket.get_rect()
    rocket_rect.center = screen_rect.center
    rocket_rect.left = 300
    return rocket

def updateScreen(screen, rocket):
    screen.fill((255, 255, 255))
    move_rocket(rocket.get_rect(), screen.get_rect())
    screen.blit(rocket, rocket.get_rect())
    pygame.display.flip()


def move_rocket(rocket_rect, screen_rect):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and rocket_rect.top > 0:
                rocket_rect.top -= 1.5
            elif event.key == pygame.K_DOWN and rocket_rect.bottom < screen_rect.bottom:
                rocket_rect.bottom += 1.5
            elif event.key == pygame.K_q:
                sys.exit()

if __name__ == "__main__":
    main()

