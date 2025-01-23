import pygame, sys
from settings import *
from level import Level
from overworld import Overworld
from ui import UI

class Game:
    def __init__(self):

        # game attributes
        self.max_level = 1
        self.coins = 1
        self.death_sound = pygame.mixer.Sound('audio/death.mp3')
        self.death_sound.set_volume(0.1)

        # overworld creation
        self.overworld = Overworld(1,self.max_level,screen,self.create_level)
        self.status = 'overworld'

        # user interface
        self.ui = UI(screen)

    def stop_music(self):
        pygame.mixer.music.stop()

    def create_level(self, current_level):
        self.level = Level(current_level,screen,self.create_overworld,self.change_coins)
        self.status = 'level'

    def create_overworld(self,current_level,new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level,self.max_level,screen,self.create_level)
        self.status = 'overworld'

    def change_coins(self,amount):
        self.coins = max(0, self.coins + amount)

    def check_game_over(self):
        if self.coins <= 0:
            self.death_sound.play()
            self.stop_music()
            self.coins = 1
            self.max_level = 1
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'


    def run(self):
        if self.status =='overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_coins(self.coins)
            self.check_game_over()

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')
    game.run()

    pygame.display.update()
    clock.tick(60)
