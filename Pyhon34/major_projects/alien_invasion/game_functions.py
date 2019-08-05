import sys
import pygame

'''  This module has game functions of Alien Invasion '''
def check_keydown_events(event, ship):
    ''' Respond to keypress '''
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = True

def check_keyup_events(event, ship):
    ''' Respond to key releases '''
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = False

def check_events(ship):
    # Respond for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def update_screen(ai_settings, screen, ship):
    ''' Update images on the screen and flip them to the new screen '''
    # Redraw the screen each pass trough the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()