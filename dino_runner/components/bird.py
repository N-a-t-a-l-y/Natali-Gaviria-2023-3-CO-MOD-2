import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

class Bird(Obstacle):
    BIRD_HEIGHTS = [260, 220, 170]
    y_random = random.choice(BIRD_HEIGHTS)
    def __init__(self, image):
        self.image = BIRD[0]
        self.bird_rect = self.image.get_rect()
        self.bird_rect.x = 600
        self.bird_rect.y = self.y_random
        self.step_index += 1
