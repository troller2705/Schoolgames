import pygame
from spritesheet_functions import SpriteSheet

#   Name of file
#   X location of sprite
#   Y location of sprite

sprite_size = 16, 16

top_left = (0, 0, 16, 16)
top_middle = (16, 0, 16, 16)
top_right = (32, 0, 16, 16)
middle_left = (0, 16, 16, 16)
middle_middle = (16, 16, 16, 16)
middle_right = (32, 16, 16, 16)
bottom_left = (0, 32, 16, 16)
bottom_middle = (16, 32, 16, 16)
bottom_right = (32, 32, 16, 16)

human


class Assets(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        sprite_sheet = SpriteSheet("Assets/Bricks-16x16.png")

        img = sprite_sheet.get_image(sprite_sheet_data[0],
                                     sprite_sheet_data[1],
                                     sprite_sheet_data[2],
                                     sprite_sheet_data[3])
        self.image = pygame.transform.scale(img, (32, 32))

        self.rect = img.get_rect()
