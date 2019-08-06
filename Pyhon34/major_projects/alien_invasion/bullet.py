import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' A class to managa the bullets from ship '''

    def __init__(self, ai_settings, screen, ship):
        ''' Creating a bullet object at the position of the ship '''
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating a bullet at the position (0, 0) and putting it at a right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speep_factor = ai_settings.bullet_speed_factor

    def update(self):
        ''' Move the ship up to the screen '''
        # Update the decimal position of the bullet
        self.y -= self.speep_factor
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        ''' Draw the bullet on the screen '''
        pygame.draw.rect(self.screen, self.color, self.rect)