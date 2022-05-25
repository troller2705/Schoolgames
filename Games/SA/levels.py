import pygame

import constants
import mapping_assets


class Level:
    def __init__(self, player):
        self.block_list = None
        self.enemy_list = None
        self.loot_list = None
        self.x = None
        self.b = None
        self.p = None
        self.e = None
        self.h = None
        self.d = None

        # Background image
        self.background = pygame.image.load("./Assets/Water-BG.jpeg")

        self.block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.loot_list = pygame.sprite.Group()
        self.player = player

        # Update everything on this level
        def update(self):
            """ Update everything in this level."""
            self.block_list.update()
            self.enemy_list.update()
            self.loot_list.update()

        def draw(self, screen):
            """ Draw everything on this level. """
            # Draw all the sprite lists that we have
            self.block_list.draw(screen)
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
        x = self.x
        b = self.b
        p = self.p
        e = self.e
        h = self.h
        d = self.d

        lvl = [[b, b, b, b, b, b, b, x, b, b, b, b, b, b, b],
               [b, h, x, x, x, x, b, x, b, x, b, x, x, h, b],
               [b, x, x, b, x, b, b, x, b, x, x, x, x, x, b],
               [b, x, x, b, x, x, x, x, x, x, x, x, x, b, b],
               [b, b, x, b, b, x, b, b, b, x, x, b, b, b, b],
               [b, x, x, x, x, x, x, x, x, x, x, x, x, x, b],
               [b, b, b, b, b, x, b, d, b, x, b, x, b, b, b],
               [x, x, x, x, b, x, b, e, b, x, b, x, x, x, x],
               [b, b, b, x, b, x, b, b, b, x, b, b, b, b, b],
               [b, x, x, x, x, x, x, p, x, x, x, x, x, x, b],
               [b, b, b, b, x, x, b, b, b, x, x, b, x, x, b],
               [b, x, x, b, x, x, x, x, x, x, x, b, b, x, b],
               [b, x, x, b, x, x, b, x, b, x, x, x, x, x, b],
               [b, h, x, x, x, x, b, x, b, x, x, b, x, h, b],
               [b, b, b, b, b, b, b, x, b, b, b, b, b, b, b]]

        for row in lvl:
            for col in row:
                if col == b:
                    self.brick = mapping_assets.b
                if col == d:
                    pass
                if col == p:
                    pass
                if col == h:
                    self.human = mapping_assets.h
                if col == e:
                    pass
                if col == x:
                    pass

            # self.block = platforms.Platform(platform[0])
            # self.block.rect.x = platform[1]
            # self.block.rect.y = platform[2]
            # self.block.player = self.player
            # self.platform_list.add(self.block)

