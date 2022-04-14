import SpriteSheet


class Enemies:
    def __init__(self):
        self.Speed = 5
        self.HP = 1
        self.Damage = 1
        self.x = None
        self.y = None
        self.image = None
        self.player = None

    def sprite(self):
        # This is the sprite sheet for the enemies
        self.sprite_sheet = SpriteSheet.spritesheet("Images/Enemies.png")

    def death(self):
        if self.HP <= 0:
            # todo: death animation
            pass

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.player, (self.x, self.y))

    def attack(self):
        self.player.HP -= self.Damage
