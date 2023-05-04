import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.utils.constants import SHIELD_TYPE

class PowerupManager:
    def __init__(self, game):
        self.powerups = []
        self.duration = random.randint(3, 5)
        self.appears_when = random.randint(50, 70) #score btween 50 and 7'

    def update(self, game):
        if len(self.powerups) == 0 and self.appears_when == game.score.count:
            self.generate_powerup()
        for powerup in self.powerups:
            powerup.update(game.game_speed, self.powerups)
            if game.player.dino_rect.colliderect(powerup.rect):
                self.powerups.remove(powerup)
                powerup.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.type = SHIELD_TYPE
                game.player.time = powerup.start_time + (self.duration * 100)

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)


    def reset_powerups(self, game):
        self.powerups[]
        self.appears_when = random.randint(50, 70)

    def generate_powerup(self):
        self.appears_when = random.randint(200, 300)
        powerup = Shield()
        self.powerups.append(powerup)