import pygame
from spritesheet_functions import SpriteSheet

#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

tl = (0, 0, 16, 16)
tm = (16, 0, 16, 16)
tr = (32, 0, 16, 16)
ml = (0, 16, 16, 16)
mm = (16, 16, 16, 16)
mr = (32, 16, 16, 16)
bl = (0, 32, 16, 16)
bm = (16, 32, 16, 16)
br = (32, 32, 16, 16)

h = pygame.image.load("./Characters/Swimmer.png")


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
