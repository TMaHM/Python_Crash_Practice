import sys

import pygame


def run_practice():
    pygame.init()
    width = 1200
    height = 800
    color = (0, 255, 255)

    p_screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("Julia")

    image = pygame.image.load('images/saber.bmp')
    rect = image.get_rect()
    p_screen_rect = p_screen.get_rect()

    rect.center = p_screen_rect.center

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        p_screen.fill(color)

        p_screen.blit(image, rect)

        pygame.display.flip()



run_practice()