import pygame


class Character:
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/dino.bmp')
        self.rect = self.image.get_rect()
        self.rect.center =self.screen_rect.center
    def blitme(self): #making the image on the top of the display attribute
        self.screen.blit(self.image, self.rect)