import pygame

import constants
import mapping_assets


class Level:
    def __init__(self, player, enemy):
        self.block_list = None
        self.enemy_list = None
        self.loot_list = None

        # Background image
        self.background = pygame.image.load("./Assets/Water-BG.jpeg")

        self.block_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.loot_list = pygame.sprite.Group()
        self.player = player
        self.enemy = enemy

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
    def __init__(self, player, enemy):
        """ Create level 1. """
        x, y = 0, 0
        # Call the parent constructor
        Level.__init__(self, player, enemy)

        lvl = [["b", "b", "b", "b", "b", "b", "b", "x", "b", "b", "b", "b", "b", "b", "b"],
               ["b", "h", "x", "x", "x", "x", "b", "x", "b", "x", "b", "x", "x", "h", "b"],
               ["b", "x", "x", "b", "x", "b", "b", "x", "b", "x", "x", "x", "x", "x", "b"],
               ["b", "x", "x", "b", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b", "b"],
               ["b", "b", "x", "b", "b", "x", "b", "b", "b", "x", "x", "b", "b", "b", "b"],
               ["b", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "b"],
               ["b", "b", "b", "b", "b", "x", "b", "d", "b", "x", "b", "x", "b", "b", "b"],
               ["x", "x", "x", "x", "b", "x", "b", "e", "b", "x", "b", "x", "x", "x", "x"],
               ["b", "b", "b", "x", "b", "x", "b", "b", "b", "x", "b", "b", "b", "b", "b"],
               ["b", "x", "x", "x", "x", "x", "x", "p", "x", "x", "x", "x", "x", "x", "b"],
               ["b", "b", "b", "b", "x", "x", "b", "b", "b", "x", "x", "b", "x", "x", "b"],
               ["b", "x", "x", "b", "x", "x", "x", "x", "x", "x", "x", "b", "b", "x", "b"],
               ["b", "x", "x", "b", "x", "x", "b", "x", "b", "x", "x", "x", "x", "x", "b"],
               ["b", "h", "x", "x", "x", "x", "b", "x", "b", "x", "x", "b", "x", "h", "b"],
               ["b", "b", "b", "b", "b", "b", "b", "x", "b", "b", "b", "b", "b", "b", "b"]]

        for row in lvl:
            x += 1
            for col in row:
                y += 1
                if y > 15:
                    y = 1
                if col == "b":
                    self.brick = mapping_assets.b
                    self.brick.rect.x = x
                    self.brick.rect.y = y
                    self.block_list.add(self.brick)
                if col == "d":
                    self.door = mapping_assets.b
                    self.door.rect.x = x
                    self.door.rect.y = y
                    self.block_list.add(self.door)
                if col == "p":
                    self.player_pos = self.player
                    self.player_pos.rect.x = x
                    self.player_pos.rect.y = y
                    self.block_list.add(self.player_pos)
                if col == "h":
                    self.human = mapping_assets.h
                    self.human.rect.x = x
                    self.human.rect.y = y
                    self.loot_list.add(self.human)
                if col == "e":
                    self.enemy = self.enemy
                    self.enemy.rect.x = x
                    self.enemy.rect.y = y
                    self.enemy_list.add(self.enemy)

            # self.block = platforms.Platform(platform[0])
            # self.block.rect.x = platform[1]
            # self.block.rect.y = platform[2]
            # self.block.player = self.player
            # self.platform_list.add(self.block)
