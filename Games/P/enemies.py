from spritesheet_functions import SpriteSheet
import player


class Enemies:
    def __init__(self):
        self.Player = Player.Player()
        self.Mushroom = None
        self.Speed = 5
        self.HP = 1
        self.Damage = 1
        self.x = None
        self.y = None

    def sprite(self):
        # This is the sprite sheet for the enemies
        self.Mushroom = SpriteSheet.spritesheet("Images/Enemies.png")

    def death(self):
        if self.HP <= 0:
            # todo: death animation
            pass

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, sprite, screen):
        screen.blit(sprite, (self.x, self.y))

    def attack(self):
        self.Player.HP -= self.Damage
