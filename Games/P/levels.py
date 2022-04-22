import pygame

import constants
import platforms

# Maps are 1600px wide x 800px tall


class Level:
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """

        # Lists of sprites used in all levels. Add or remove
        # lists as needed for your game.
        self.platform_list = None
        self.enemy_list = None
        self.loot_list = None

        # Background image
        self.background = None

        # How far this world has been scrolled left/right
        self.world_shift = 0
        self.level_limit = -500
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.loot_list = pygame.sprite.Group()
        self.player = player

    # Update everything on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.loot_list.update()

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.BLUE)
        screen.blit(self.background, (self.world_shift // 3, 0))

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.loot_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right, and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

    def loot(self, lvl):
        if lvl == 1:
            self.loot_list = pygame.sprite.Group()
            loot = Platform(tx * 9, ty * 5, tx, ty, "Assets/Decor/Items.png")
            self.loot_list.add(loot)

        if lvl == 2:
            print(lvl)

        return self.loot_list


# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/BG/BG1.png").convert()
        self.background.set_colorkey((255, 255, 255))

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.GRASS_LEFT, 500, 600],
                 [platforms.GRASS_MIDDLE, 530, 600],
                 [platforms.GRASS_MIDDLE, 560, 600],
                 [platforms.GRASS_MIDDLE, 590, 600],
                 [platforms.GRASS_MIDDLE, 620, 600],
                 [platforms.GRASS_RIGHT, 640, 600],
                 [platforms.GRASS_LEFT, 800, 450],
                 [platforms.GRASS_MIDDLE, 830, 450],
                 [platforms.GRASS_MIDDLE, 860, 450],
                 [platforms.GRASS_MIDDLE, 890, 450],
                 [platforms.GRASS_MIDDLE, 920, 450],
                 [platforms.GRASS_RIGHT, 940, 450],
                 [platforms.GRASS_LEFT, 1000, 500],
                 [platforms.GRASS_MIDDLE, 1030, 500],
                 [platforms.GRASS_MIDDLE, 1060, 500],
                 [platforms.GRASS_MIDDLE, 1090, 500],
                 [platforms.GRASS_MIDDLE, 1120, 500],
                 [platforms.GRASS_RIGHT, 1140, 500],
                 [platforms.GRASS_LEFT, 1100, 350],
                 [platforms.GRASS_MIDDLE, 1130, 350],
                 [platforms.GRASS_MIDDLE, 1160, 350],
                 [platforms.GRASS_MIDDLE, 1190, 350],
                 [platforms.GRASS_MIDDLE, 1220, 350],
                 [platforms.GRASS_RIGHT, 1240, 350]]

        # Go through the array above and add platforms
        for platform in level:
            self.block = platforms.Platform(platform[0])
            self.block.rect.x = platform[1]
            self.block.rect.y = platform[2]
            self.block.player = self.player
            self.platform_list.add(self.block)


# Create platforms for the level
class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/BG/background.png").convert()
        self.background.set_colorkey((255, 255, 255))

        # Array with type of platform, and x, y location of the platform.
        level = [[platforms.GRASS_LEFT, 500, 600],
                 [platforms.GRASS_MIDDLE, 530, 600],
                 [platforms.GRASS_MIDDLE, 560, 600],
                 [platforms.GRASS_MIDDLE, 590, 600],
                 [platforms.GRASS_MIDDLE, 620, 600],
                 [platforms.GRASS_RIGHT, 640, 600],
                 [platforms.GRASS_LEFT, 800, 450],
                 [platforms.GRASS_MIDDLE, 830, 450],
                 [platforms.GRASS_MIDDLE, 860, 450],
                 [platforms.GRASS_MIDDLE, 890, 450],
                 [platforms.GRASS_MIDDLE, 920, 450],
                 [platforms.GRASS_RIGHT, 940, 450],
                 [platforms.GRASS_LEFT, 1000, 500],
                 [platforms.GRASS_MIDDLE, 1030, 500],
                 [platforms.GRASS_MIDDLE, 1060, 500],
                 [platforms.GRASS_MIDDLE, 1090, 500],
                 [platforms.GRASS_MIDDLE, 1120, 500],
                 [platforms.GRASS_RIGHT, 1140, 500],
                 [platforms.GRASS_LEFT, 1100, 350],
                 [platforms.GRASS_MIDDLE, 1130, 350],
                 [platforms.GRASS_MIDDLE, 1160, 350],
                 [platforms.GRASS_MIDDLE, 1190, 350],
                 [platforms.GRASS_MIDDLE, 1220, 350],
                 [platforms.GRASS_RIGHT, 1240, 350]]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
