import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    BIRD_HEIGHTS = [260, 220, 170]
    y_random = random.choice(BIRD_HEIGHTS)
    step_index = 0
    def __init__(self, image):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = 600
        self.bird_rect.y = self.y_random

    def update(self, game_speed, obstacles):
        return super().update(game_speed, obstacles)

    def fly(self):
        self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
        self.bird_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

