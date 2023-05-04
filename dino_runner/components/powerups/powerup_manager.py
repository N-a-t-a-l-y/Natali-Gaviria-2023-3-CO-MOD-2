import random
import pygame
from dino_runner.components.powerups.shield import Shield
from dino_runner.components.powerups.hammer import Hammer

class PowerupManager:                                                                                      #metodo constructor
    def __init__(self):                                                                                 #lista vacia
        self.powerups = []
        self.duration = random.randint(3, 5)                                                            #duracion random entre  3 to 5 segs                
        self.appears_when = random.randint(50, 70)    #score btween 50 and 7'

    def update(self, game):                                                             #metodo que permite usar la clase game.py
        if len(self.powerups) == 0 and self.appears_when == game.score.count:  #si la lista está vacia y si el valor de "appears_when" es igual al valor actual de "game.score.count".
            power = self.generate_powerup(random.randint(0, 1))                                   #se añade el powerup a la lista vacia
            self.powerups.append(power)

        for powerup in self.powerups:                       #itera en la lista
            powerup.update(game.game_speed, self.powerups)  #powerup se actualiza recibiendo metodo de game(que contiene 20) y recibiendo lo que se encuentra dentro de la lista
            if game.player.dino_rect.colliderect(powerup.rect):   #si el rectangulo del jugador colisiona con powerup.rect, eliminar de la lista el powerup
                self.powerups.remove(powerup)
                powerup.start_time = pygame.time.get_ticks() #el metodo start_time de powerup cambia su valor al de obtener el tiempo trasncurrido en milisegundos 
                game.player.has_power_up = True             #al colisionar y remover el item del powerup, activamos a true que el dino ya tiene un powerup
                game.player.type = powerup.type
                game.player.power_up_time = powerup.start_time + (self.duration * 1000)   #guarda en power_up_time el tiempo total que mantendrá activado el powerup

    def draw(self, screen):
        for powerup in self.powerups:
            powerup.draw(screen)


    def reset_powerups(self, game):
        self.powerups = []
        self.appears_when = random.randint(50, 70)

    def generate_powerup(self, powerup_type):
        self.appears_when = random.randint(200, 300)
        if powerup_type == 0:
            powerup = Shield()
        elif powerup_type == 1:
            powerup = Hammer()
        return powerup
