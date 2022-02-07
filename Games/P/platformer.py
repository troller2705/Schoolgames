import pygame
# 3+ lives


class Player:
    def __init__(self):
        self.HP = 3 + self.Gain
        self.Damage = 1
        self.Speed = 15
        self.Gain = 0  # Stats increase per level(+10HP, +5 Damage, +5 Speed), Difficulty of enemies is same as level


class Enemies:
    def __init__(self):
        self.Speed = 5
        self.HP = 1
        self.Damage = 1


class Platformer:

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
            self.game.display.fill(self.game.RED)
            self.game.draw_text('Platformer', 40, self.mid_w, self.mid_h)
            self.game.display.blit(self.game.display, (0, 0))
            pygame.display.update()
            self.game.reset_keys()
