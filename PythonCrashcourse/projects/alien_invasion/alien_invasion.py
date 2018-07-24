import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from enemy_ship import EnemyShip


def run_game():
    # initialize game and create a screen object
    pygame.init()
    # make dimensions for the screen
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_settings, screen)
    # make an enemy ship
    enemy_ship = EnemyShip(ai_settings, screen)
    # make a group to store bullets in.
    bullets = Group()
    # start the main loop for the game
    while True:
        # watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, enemy_ship, ship, bullets)


run_game()
