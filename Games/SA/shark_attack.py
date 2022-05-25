import pygame

import constants
import levels

from player import Player


class main:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        DISPLAY_W, DISPLAY_H = pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1]
        self.display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H), pygame.FULLSCREEN)
        SA_Icon = pygame.image.load('./Assets/icon.png')
        pygame.display.set_icon(SA_Icon)
        pygame.display.set_caption("Shark Attack")
        # Create the player
        self.player = Player()

        # Create all the levels
        self.level_list = [levels.Level_01(self.player)]

        # Set the current level
        self.current_level_no = 0
        self.current_level = self.level_list[self.current_level_no]

        self.active_sprite_list = pygame.sprite.Group()
        self.player.level = self.current_level
        self.active_sprite_list.add(self.player)

        # Loop until the user clicks the close button.
        self.done = False

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

    def text(self, font, text, size, x, y):
        font = pygame.font.Font(font, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)

    def game(self):
        main.__init__(self)
        # -------- Main Program Loop -----------
        while not self.done:
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.go_left()
                    if event.key == pygame.K_RIGHT:
                        self.player.go_right()

            # Update the player.
            self.active_sprite_list.update()

            # Update items in the level
            self.current_level.update()

            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.current_level.draw(screen)
            self.active_sprite_list.draw(screen)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.
        pygame.quit()


if __name__ == "__main__":
    main().game()
