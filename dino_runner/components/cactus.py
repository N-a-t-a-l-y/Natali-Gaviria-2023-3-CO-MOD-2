import random
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS

class Cactus(Obstacle):
    def __init__(self):
        self.small_cactus = SMALL_CACTUS
        self.large_cactus = LARGE_CACTUS
        self.list = (self.small_cactus, self.large_cactus)
        self.type = random.randint(0, 2)
        image = random.choice(self.list)
        super().__init__(image, self.type)
        self.rect.y = 325
