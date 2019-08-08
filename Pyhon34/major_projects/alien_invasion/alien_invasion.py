import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # Initialize pygame, settings and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets and group that stores aliens
    bullets = Group()
    aliens = Group()
    pygame.display.set_caption('Alien Invasion')

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()