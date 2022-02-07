import pygame
# 3 Lives


class Player:
    def __init__(self):
        self.HP = 3
        self.Damage = 1
        self.Speed = 15


class Enemies:
    def __init__(self):
        self.Speed = 5
        self.HP = 1
        self.Damage = 1


class SharkAttack:

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
            self.game.display.fill(self.game.GREEN)
            self.game.draw_text('Shark Attack', 40, self.mid_w, self.mid_h)
            self.game.display.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.reset_keys()
