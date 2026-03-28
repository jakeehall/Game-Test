import random
import pygame
from src.utils.asset_loader import load_image

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = load_image("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (
            random.randint(
                40 + (self.rect.width // 2),
                self.game.screen_width - 40 - (self.rect.width // 2)
            ),
            0
        )


    def move(self):
        self.rect.move_ip(0, self.game.speed)
        if (self.rect.top >= self.game.screen_height):
            self.game.score += 1
            self.rect.midbottom = (
                random.randint(
                    40 + (self.rect.width // 2),
                    self.game.screen_width - 40 - (self.rect.width // 2)
                ),
                0
            )