import pygame

import game
import levels

from Player import Player


class Platformer:

    def __init__(self, game):
        self.playing = game.playing
        self.x, self.y = self.game.display.get_size()
        self.mid_w, self.mid_h = self.x / 2, self.y / 2

        # Create the player
        self.player = Player()

        # Create all the levels
        self.level_list = [levels.Level_01(self.player), levels.Level_02(self.player)]

        # Set the current level
        self.current_level_no = 0
        self.current_level = self.level_list[self.current_level_no]

        active_sprite_list = pygame.sprite.Group()
        self.player.level = self.current_level

        self.player.rect.x = 340
        self.player.rect.y = self.game.DISPLAY_H - self.player.rect.height
        active_sprite_list.add(self.player)

    def game_loop(self):
        while self.playing:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.playing = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.go_right()
                    if event.key == pygame.K_UP:
                        self.player.jump()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player.change_x < 0:
                        self.player.stop()
                    if event.key == pygame.K_RIGHT and player.change_x > 0:
                        self.player.stop()

            # Update the player.
            active_sprite_list.update()

            # Update items in the level
            self.current_level.update()

            # If the player gets near the right side, shift the world left (-x)
            if self.player.rect.right >= 500:
                diff = self.player.rect.right - 500
                self.player.rect.right = 500
                self.current_level.shift_world(-diff)

            # If the player gets near the left side, shift the world right (+x)
            if self.player.rect.left <= 120:
                diff = 120 - self.player.rect.left
                self.player.rect.left = 120
                self.current_level.shift_world(diff)

            # If the player gets to the end of the level, go to the next level
            current_position = player.rect.x + self.current_level.world_shift
            if current_position < self.current_level.level_limit:
                self.player.rect.x = 120
                if self.current_level_no < len(self.level_list) - 1:
                    self.current_level_no += 1
                    self.current_level = self.level_list[selfcurrent_level_no]
                    self.player.level = self.current_level

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.current_level.draw(screen)
            active_sprite_list.draw(screen)

            pygame.display.update()
            self.game.reset_keys()
