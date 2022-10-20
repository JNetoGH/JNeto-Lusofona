import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((400, 400));

red = 0
blue = 0
green = 0

incremento_de_cor = 10

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            # armazena numa lista as telcas pressionadas
            keys = pygame.key.get_pressed()

            if keys [pygame.K_r] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                red = red - incremento_de_cor
            elif event.key == pygame.K_r:
                red = red + incremento_de_cor

            elif keys [pygame.K_b] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                blue = blue - incremento_de_cor
            elif event.key == pygame.K_b:
                blue = blue + incremento_de_cor

            elif keys [pygame.K_g] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
                green = green - incremento_de_cor
            elif event.key == pygame.K_g:
                green = green + incremento_de_cor

            elif event.key == pygame.K_0:
                red = 0
                blue = 0
                green = 0

    # protecao anti-crash, caso cor seja invalida trava o incremento/decremento
    if red > 255:
        red = 255
    elif red < 0:
        red = 0

    if blue > 255:
        blue = 255
    elif blue < 0:
        blue = 0

    if green > 255:
        green = 255
    elif green < 0:
        green = 0

    print(f"cor atual (r:{red}, b:{blue}, g:{green})")
    DISPLAY_SURF.fill((red,green, blue))

    pygame.display.update()