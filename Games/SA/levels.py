import pygame

import constants
import mapping_assets


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


class Level_01(Level):
    """ Definition for level 1. """
    # 0 = empty space
    # 1 = wall
    # 2 = player
    # 3 = enemy
    # 4 = human


