import pygame


class Platformer:

    def __init__(self, game):
        self.playing = game.playing
        self.x, self.y = self.game.display.get_size()
        self.mid_w, self.mid_h = self.x / 2, self.y / 2

    def game_loop(self):
        while self.playing:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.playing = False
            self.game.display.fill(self.game.RED)

            pygame.display.update()
            self.game.reset_keys()
