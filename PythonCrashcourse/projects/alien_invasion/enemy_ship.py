import pygame
from pygame.sprite import Sprite


class EnemyShip(Sprite):
    """A class to represent a single enemy ship in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initizalize the enemy ship set its starting position"""
        super(EnemyShip, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('imgs/alien.bmp')
        self.rect = self.image.get_rect()
        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the enemy ship at its current location."""
        self.screen.blit(self.image, self.rect)