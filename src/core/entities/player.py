import pygame
from pygame.locals import K_LEFT, K_RIGHT
from src.utils.asset_loader import load_image

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = load_image("player.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (
            self.game.screen_width // 2,
            self.game.screen_height - 15
        )


    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 40:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < (self.game.screen_width - 40):     
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)