import pygame, sys
from pygame.locals import *
import math
import numpy

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((400, 400))

CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)

# valor inicial em X
# mas tb é incrementado acada update representado a posição em x atual do ponto da linha a ser desenhado
x = 10
angle = 0

# valor inicial em Y
# é somado em cada update ao cos do angulo para dar a variação em y do ponto da linha a ser desenhado
my_line_y1 = 50
my_line_y2 = 100

amplitude = 10

# is changed via user input
my_lines_fases = numpy.pi  # Deslocamento da origem do gráfico

my_line1_frequency = 2
my_line2_frequency = 4

while True:  # Main loop--

    # INCREMENTS X AND THE ANGLE
    x = x + 1
    angle = angle + 0.1

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_RIGHT or event.key == pygame.K_a:
                # CLEARS THE SCREEN
                DISPLAY_SURF.fill((0, 0, 0))
                # RESETS THE LINE WITH A NEW FASE
                my_lines_fases += 0.1
                x = 10
                my_line_y1 = 50
            if event.key == pygame.K_LEFT or event.key == pygame.K_d:
                # CLEARS THE SCREEN
                DISPLAY_SURF.fill((0, 0, 0))
                # RESETS THE LINE WITH A NEW FASE
                my_lines_fases -= 0.1
                x = 10
                my_line_y2 = 100
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # DRAWING MY LINES
    pygame.draw.circle(DISPLAY_SURF, CYAN,
                       [x, my_line_y1 + amplitude * math.cos(angle * my_line1_frequency + my_lines_fases)], 1)
    pygame.draw.circle(DISPLAY_SURF, YELLOW,
                       [x, my_line_y2 + amplitude * math.cos(angle * my_line2_frequency + my_lines_fases)], 1)

    pygame.display.update()
