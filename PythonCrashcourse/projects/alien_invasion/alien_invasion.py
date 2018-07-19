import sys

import pygame


def run_game():
    # iniciar juego y crear un objeto pantalla
    pygame.init()
    # creando dimensiones de la pantalla
    screen = pygame.display.set_mode((1200, 800))

    # iniciando el ciclo principal del juego
    while True:

        # mirar eventos del teclado y mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # hacer visible el ultimo dibujo mosrado en la pantalla
        pygame.display.flip()

run_game()