import pygame
def creat_screen():
    pygame.init()
    screen = pygame.display.set_mode((700,500))
    pygame.display.set_caption("event_type")
    screen.fill((255, 255, 255))

def print_event_type():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(f"\033[35m{event.key}\033[m")

if __name__ == "__main__":
    creat_screen()
    while True:
        print_event_type()