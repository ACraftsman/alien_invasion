import pygame
import sys
def create_rocket():
    pygame.init()
    # 使用该函数可以实现按键的连续检测，第一个参数影响着按键的灵敏度，第二个参数影响着按键的移动时间间隔
    pygame.key.set_repeat(10, 15)
    screen = pygame.display.set_mode((700,550))
    pygame.display.set_caption("Rocket")
    rocket = pygame.image.load("images/rocket.jpg")
    rocket = pygame.transform.scale(rocket, (60, 80))
    rocket_rect = rocket.get_rect()
    rocket_rect.center = screen.get_rect().center
    screen_rect = screen.get_rect()
    while True:
        check_key_boades(rocket_rect, screen_rect)
        screen.fill((255, 255, 255))
        screen.blit(rocket, rocket_rect)
        pygame.display.flip()


def check_key_down(event, rocket_rect, screen_rect):
    if event.key == pygame.K_RIGHT:
        if rocket_rect.right + 1.5 <= screen_rect.right:
            rocket_rect.right += 1.5
    elif event.key == pygame.K_LEFT:
        if rocket_rect.left - 1.5 >= 0:
            rocket_rect.left -= 1.5
    elif event.key == pygame.K_UP:
        if rocket_rect.top - 1.5 >= 0:
            rocket_rect.top -= 1.5
    elif event.key == pygame.K_DOWN:
        if rocket_rect.bottom + 1.5 <= screen_rect.bottom:
            rocket_rect.bottom += 1.5

def check_key_boades(rocket_rect, screen_rect):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, rocket_rect, screen_rect)

if __name__ == "__main__":
    create_rocket()