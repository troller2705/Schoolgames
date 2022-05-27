import pygame


class Player:
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        super().__init__()

        # -- Attributes
        self.lives = 5
        # Set effects of player
        self.player = None
        self.invincible = False
        self.invincible_timer = 5

        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
        self.size = (150, 150)
        self.x = 50
        self.y = 50

        # What direction is the player facing?
        self.direction = "R"

        self.img = "./Characters/Shark.R.png"

        # List of sprites we can bump against
        self.level = None

    def update(self):
        """ Move the player. """
        # Move left/right
        self.x += self.change_x
        # Move up/down
        self.y += self.change_y

        if self.direction == "L":
            self.img = "./Characters/Shark.L.png"
        elif self.direction == "R":
            self.img = "./Characters/Shark.R.png"
        elif self.direction == "U":
            self.img = "./Characters/Shark.U.png"
        elif self.direction == "D":
            self.img = "./Characters/Shark.D.png"

        """# See if we hit anything
        block_hit_list = self.rect.colliderect(self, self.level.block_list)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise, if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Check and see if we hit anything
        block_hit_list = self.rect.colliderect(self, self.level.block_list)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom"""

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -2
        self.change_y = 0
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 2
        self.change_y = 0
        self.direction = "R"

    def go_up(self):
        self.change_y = -2
        self.change_x = 0
        self.direction = "U"

    def go_down(self):
        self.change_y = 2
        self.change_x = 0
        self.direction = "D"

    def draw_player(self, display):
        self.player = pygame.image.load(self.img)
        player = pygame.transform.scale(self.player, self.size)
        display.blit(player, [self.x, self.y])

    def death(self):
        self.lives -= 1
        self.x = 50
        self.y = 50
