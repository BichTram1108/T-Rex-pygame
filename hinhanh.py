import pygame
import os

#Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

RUNNING = [pygame.image.load(os.path.join("picture/Dino", "DinoRun1.png")), 
            pygame.image.load(os.path.join("picture/Dino", "DinoRun2.png"))]

JUMPING = pygame.image.load(os.path.join('picture/Dino', 'DinoJump.png'))

DUCKING = [pygame.image.load(os.path.join("picture/Dino", "DinoDuck1.png")), 
            pygame.image.load(os.path.join("picture/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("picture/Cactus", "SmallCactus1.png")), 
            pygame.image.load(os.path.join("picture/Cactus", "SmallCactus2.png")),
            pygame.image.load(os.path.join("picture/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("picture/Cactus", "LargeCactus1.png")), 
            pygame.image.load(os.path.join("picture/Cactus", "LargeCactus2.png")),
            pygame.image.load(os.path.join("picture/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("picture/Bird", "Bird1.png")), 
            pygame.image.load(os.path.join("picture/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join('picture/Other', 'Cloud.png'))

BG = pygame.image.load(os.path.join('picture/Other', 'Track.png'))