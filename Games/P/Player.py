import SpriteSheet as spritesheet


class Player:
    def __init__(self):
        self.image = None
        self.player = None
        self.y = None
        self.x = None
        self.lives = 3
        self.HP = 1
        self.Damage = 1
        self.Speed = 15

    def sprite(self):
        self.player = spritesheet.spriteshee('Mario Files/Characters/Mario.png')
        self.image = self.player.image_at((0, 0, 16, 16))

    def death(self):
        if self.HP <= 0:
            self.lives -= 1
            self.HP = 1
            if self.lives <= 0:
                print("You died")
                exit()

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.player, (self.x, self.y))

    def attack(self, enemy):
        enemy.HP -= self.Damage
        print("You attacked the enemy")
        self.death()