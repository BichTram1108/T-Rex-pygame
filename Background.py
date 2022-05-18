from lib2to3.pygram import python_grammar_no_print_statement
from tkinter import image_names
from tkinter.font import BOLD
import pygame
import os
from hinhanh import *


pygame.init()
class Background_2:
    """Lớp hình nền level 2"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 14
        self.img = BG3
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self, SCREEN):
        SCREEN.blit(self.img, (int(self.x), int(self.y)))
        SCREEN.blit(self.img, (int(self.x + self.width), int(self.y)))
    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x += self.width

class Background_3:
    """lớp hình nền level 3"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 14
        self.img = BG2
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    def draw(self, SCREEN):
        SCREEN.blit(self.img, (int(self.x), int(self.y)))
        SCREEN.blit(self.img, (int(self.x + self.width), int(self.y)))
    def update(self):
        self.x -= self.speed
        if self.x < -self.width:
            self.x += self.width
        
