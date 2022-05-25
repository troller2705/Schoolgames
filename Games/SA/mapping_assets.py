import pygame
from spritesheet_functions import SpriteSheet

brick = pygame.image.load("./Assets/Bricks-16x16.png")
b = pygame.transform.scale(brick, (150, 150))

human = pygame.image.load("./Characters/Swimmer.png")
h = pygame.transform.scale(human, (150, 150))

