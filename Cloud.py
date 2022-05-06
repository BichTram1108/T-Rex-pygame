import pygame
import os
import random
from hinhanh import *
pygame.init()

class Cloud:
    
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        global game_speed
        game_speed = 14
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)


    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.x, self.y))
