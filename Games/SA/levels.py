import pygame

import constants
import mapping_assets


class Level:
    def __init__(self):
        self.platform_list = None
        self.enemy_list = None
        self.loot_list = None

        # Background image
        self.background = None

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
            # Draw all the sprite lists that we have
            self.platform_list.draw(screen)
            self.enemy_list.draw(screen)
            self.loot_list.draw(screen)


class Level_01(Level):
    """ Definition for level 1. """
    # x = empty space
    # b = bricks
    # p = player
    # e = enemy
    # h = human
    # d = door
    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("Assets/BG/BG1.png").convert()
        self.background.set_colorkey((255, 255, 255))
        lvl = [[b, b, b, b, b, b, b, x, b, b, b, b, b, b, b],
               [b, x, x, x, x, x, b, x, b, x, x, x, x, x, b],
               [b, x, x, x, x, x, b, x, b, x, x, x, x, x, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, b, b, x, x, x, b, d, b, x, x, x, b, b, b],
               [x, x, x, x, x, x, b, e, b, x, x, x, x, x, x],
               [b, b, b, x, x, x, b, b, b, x, x, x, b, b, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, x, x, x, x, x, b, x, b, x, x, x, x, x, b],
               [b, x, x, x, x, x, b, x, b, x, x, x, x, x, b],
               [b, b, b, b, b, b, b, x, b, b, b, b, b, b, b]]

        for row in lvl:
            for col in lvl:
                pass

