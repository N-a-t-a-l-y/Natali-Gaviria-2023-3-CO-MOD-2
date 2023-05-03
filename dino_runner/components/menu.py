import pygame
from dino_runner.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_OVER

class Menu:
    half_screen_width = SCREEN_WIDTH // 2
    half_screen_height = SCREEN_HEIGHT // 2
    def __init__(self, screen, message):
        screen.fill((255,255,255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.font_list_end = self.font.Font(FONT_STYLE, 20)
        self.text_list_end 
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.x = self.half_screen_width
        self.text_rect.y = self.half_screen_height
        self.text_rect.center = (self.half_screen_width, self.half_screen_height) #hacia abajo lo añadi
        self.maxim_score = 0

    def update(self, game):
        self.hundle_event_on_menu(game)
        pygame.display.update()

    def draw(self, screen, deaths, score):
        data = self.font.render(data_player, True, (0, 0, 0, 0))
        if score > self.maxim_score:
            self.maxim_score = score
        data_player = f""" Score = {score}
                           Deaths = {deaths}
                         Maxim score = {self.maxim_score}"""
        data_game = self.

        screen.blit(self.text, self.text_rect)
        if deaths > 0:
            screen.blit(GAME_OVER, (self.half_screen_width - 150, self.half_screen_height - 50))

        


    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))


    def hundle_event_on_menu(self, game): #(NO TENIA USER_INPUT)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.gameruning = False
                game.playing = False
                game.deaths += 1
            elif event.type == pygame.KEYDOWN:   #1
                if event.key == pygame.K_v and not game.run():
                    game.execute()                  #2(game.run())