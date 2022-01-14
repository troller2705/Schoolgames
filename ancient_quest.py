import pygame


class AncientQuest:

    def __init__(self, game):
        self.playing = game.playing
        self.game = game
        self.x, self.y = self.game.display.get_size()
        self.mid_w, self.mid_h = self.x / 2, self.y / 2

    def game_loop(self):
        while self.playing:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.playing = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Ancient Quest', 40, self.mid_w, self.mid_h)
            self.game.display.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.reset_keys()
