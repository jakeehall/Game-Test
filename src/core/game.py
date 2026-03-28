#Imports
import time
import pygame
from pygame.locals import QUIT
from src.utils.asset_loader import load_image, load_sound
from src.core.entities.player import Player
from src.core.entities.enemy import Enemy

class Game:
    def __init__(self, screen_width=400, screen_height=600, fps=60, title="Window"):
        #Set screen width and height
        self.screen_width = screen_width
        self.screen_height = screen_height

        #Set frames per second
        self.fps = fps

        #Initializing
        pygame.init()

        #Set up clock and fps
        self.clock = pygame.time.Clock()

        #Create screen
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)

        #Set background
        self.background = load_image("street.png")

        #Set sounds
        self.crash_sound = load_sound('crash.wav')

        #Set running state to True
        self.running = True


    def run(self):
        #Set colors
        self.RED   = (255, 0, 0)
        self.BLACK = (0, 0, 0)

        #Game variables
        self.speed = 5
        self.score = 0

        #Make screen white
        self.screen.fill(self.BLACK)

        #Set fonts
        self.font_large = pygame.font.SysFont("Verdana", 60)
        self.font_small = pygame.font.SysFont("Verdana", 20)

        #Create sprites
        self.player = Player(self)
        self.enemy = Enemy(self)

        #Set enemies sprite group and add enemy sprites to the group
        enemy_group = pygame.sprite.Group()
        enemy_group.add(self.enemy)

        #Set a new user event
        self.INC_SPEED = pygame.USEREVENT + 1

        #Trigger event every x milliseconds
        pygame.time.set_timer(self.INC_SPEED, 1000)

        #Game loop
        while self.running:
            #Cycles through all events occurring
            for event in pygame.event.get():
                if event.type == self.INC_SPEED:
                    self.speed += 0.5
                if event.type == QUIT:
                    self.running = False

            #Draw background
            self.screen.blit(self.background, (0,0))

            #Get and draw score text
            score_text = self.font_small.render(str(self.score), True, self.BLACK)
            self.screen.blit(score_text, (10,10))

            #Move and draw player
            self.player.move()
            self.screen.blit(self.player.image, self.player.rect)

            #Moves and draws all enemies
            for enemy in enemy_group:
                enemy.move()
                self.screen.blit(enemy.image, enemy.rect)

            #If collision occurs between Player and enemies
            if pygame.sprite.spritecollideany(self.player, enemy_group):
                #Play crash sound and wait for the sound to end before continuing
                self.crash_sound.play()
                time.sleep(self.crash_sound.get_length())

                self.screen.fill(self.RED)
                self.game_over_text = self.font_large.render("Game Over", True, self.BLACK)
                self.screen.blit(
                    self.game_over_text,
                    self.game_over_text.get_rect(
                        center=(self.screen_width // 2,
                        self.screen_height // 2)
                    )
                )
                pygame.display.update()

                for enemy in enemy_group:
                    enemy.kill()

                time.sleep(2)

                self.running = False

            pygame.display.update()
            self.clock.tick(self.fps)


        #Stop pygame
        pygame.quit()