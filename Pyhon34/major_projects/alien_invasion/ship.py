import pygame


class Ship():

	def __init__(self, ai_settings, screen):
		''' Initialize ship and its starting position '''
		self.screen = screen
		self.ai_settings = ai_settings

		# Load the ship and get its rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		# put the ship at the position center bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# Store a deciaml value for the ship's center
		self.center = float(self.rect.centerx)

		# movement flag
		self.moving_right = False
		self.moving_left = False

	def update(self):
		''' Move the ship based on the movement flag '''
		# Update the ship's value center value, not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor

		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		# Update rect object form self.center
		self.rect.centerx = self.center

	def blitme(self):
		# Draw the ship at the current position
		self.screen.blit(self.image, self.rect)

