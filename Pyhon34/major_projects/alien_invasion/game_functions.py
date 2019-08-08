import sys
import pygame
from bullet import Bullet
from alien import Alien

'''  This module has game functions of Alien Invasion '''
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    ''' Respond to keypress '''
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullets(ai_settings, screen, ship, bullets):
    ''' Create a bullet if limit is not reached yet '''
    # Create a new bullet and add it to the group
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    ''' Respond to key releases '''
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move the ship to the right
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    # Respond for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_bullets(bullets):
    bullets.update()

    # Get rid of bullets that has been disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings, screen, ship, alien, bullets):
    ''' Update images on the screen and flip them to the new screen '''
    # Redraw the screen each pass trough the loop
    screen.fill(ai_settings.bg_color)

    # Redraw the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Draw the ship
    ship.blitme()
    aliens.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def create_fleet(ai_settings, screen, aliens):
    ''' Create a full fleet of aliens '''
    