import pygame
# 100 hp half heart every 10 hp lost


class Player:
    def __init__(self):
        self.HP = 100
        self.Damage = 20
        self.Speed = 15
        self.Level = 0  # Stats increase per level(+10HP, +5 Damage, +5 Speed), Difficulty of enemies is same as level
        self.Difficulty = self.Level


class Enemies:
    def __init__(self):
        Difficulty = self.Player.Difficulty
        self.Speed = 10
        if Difficulty > 5:
            self.HP = 250
            self.Damage = 50
        elif Difficulty > 0:
            self.HP = Difficulty * 50
            self.Damage = Difficulty * 10
        else:
            self.HP = 50
            self.Damage = 10
            

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
