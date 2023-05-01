import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING

																
class Dino:														
	X_POS = 80
	Y_POS = 310													
	Y_POS_DUCK = 340											
	JUMP_SPEED = 8.5
	def __init__(self):											
		self.image = RUNNING[0]
		self.dino_rect = self.image.get_rect()					
		self.dino_rect.x = self.X_POS						
		self.dino_rect.y = self.Y_POS	
		self.dino_run = True 
		self.step_index = 0
		self.dino_jump = False
		self.jump_speed = self.JUMP_SPEED
		self.dino_duck = False

	def update(self, user_imput):
		#colocar en cero el step_index si esta en diez
		if self.step_index > 10:
			self.step_index = 0
		
		# si el dino esta corriendo es True
		if self.dino_run:
			self.run()

		if self.dino_jump:
			self.jump()

		if self.dino_duck:
			self.duck(user_imput)

		if user_imput[pygame.K_UP] and not self.dino_jump:
			self.dino_jump = True
			self.dino_run = False			
		elif not self.dino_jump:
			self.dino_run = True
		if user_imput[pygame.K_DOWN] and not self.dino_jump:
			self.dino_duck = True
			self.dino_run = False

	def draw(self, screen):
		screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

	def run(self):
		self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
		self.dino_rect = self.image.get_rect()
		self.dino_rect.x = self.X_POS
		self.dino_rect.y = self.Y_POS
		self.step_index += 1

	def jump(self):
		self.image = JUMPING
		self.dino_rect.y -= self.jump_speed*4
		self.jump_speed -= 0.8
		if self.dino_rect.y > 300:
			self.dino_jump = False
			self.jump_speed = self.JUMP_SPEED
	  
	   
	def duck(self, user_imput):
		self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
		self.dino_rect = self.image.get_rect()
		self.dino_rect.x = self.X_POS
		self.dino_rect.y = self.Y_POS_DUCK
		self.step_index += 1
		if not user_imput[pygame.K_DOWN]:
			self.dino_duck = False
			self.dino_run = True
