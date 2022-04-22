import pygame

from spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

# Platforms
GRASS_LEFT = (0, 0, 16, 16)
GRASS_RIGHT = (32, 0, 16, 16)
GRASS_MIDDLE = (16, 0, 16, 16)
GRASS_LEFT_CENTER = (0, 16, 16, 16)
GRASS_RIGHT_CENTER = (32, 16, 16, 16)
GRASS_MIDDLE_CENTER = (16, 16, 16, 16)
GRASS_LEFT_BOTTOM = (0, 32, 16, 16)
GRASS_RIGHT_BOTTOM = (32, 32, 16, 16)
GRASS_MIDDLE_BOTTOM = (16, 32, 16, 16)
GRASS_INNER_CORNER_LEFT = (48, 0, 16, 16)
GRASS_INNER_CORNER_RIGHT = (64, 0, 16, 16)
GRASS_OUTER_CORNER_LEFT = (48, 32, 16, 16)
GRASS_OUTER_CORNER_RIGHT = (64, 32, 16, 16)
GRASS_SINGLE_BLOCK = (80, 32, 16, 16)


# Items
# Mushroom_R = (0, 0, 16, 16)
# Mushroom_G = (16, 0, 16, 16)
# Fire_Flower = (32, 0, 16, 16)
# Power_Star = (48, 0, 16, 16)
# Coin_1 = (0, 16, 16, 16)
# Coin_2 = (16, 16, 16, 16)
# Coin_3 = (32, 16, 16, 16)
# Coin_4 = (48, 16, 16, 16)
# Coin_5 = (0, 32, 16, 16)
# Coin_6 = (16, 32, 16, 16)
# Coin_7 = (32, 32, 16, 16)
# Coin_8 = (48, 32, 16, 16)


class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()

        sprite_sheet = SpriteSheet("Assets/Platforms/Tileset.png")

        img = sprite_sheet.get_image(sprite_sheet_data[0],
                                     sprite_sheet_data[1],
                                     sprite_sheet_data[2],
                                     sprite_sheet_data[3])
        self.image = pygame.transform.scale(img, (32, 32))

        self.rect = img.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """

    def __init__(self, sprite_sheet_data):

        super().__init__(sprite_sheet_data)

        self.change_x = 0
        self.change_y = 0

        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.level = None
        self.player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise, if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
