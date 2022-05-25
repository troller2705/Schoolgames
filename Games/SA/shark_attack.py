import pygame

import constants
import levels

from player import Player

pygame.init()
pygame.mixer.init()
DISPLAY_W, DISPLAY_H = pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1]
display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H), pygame.FULLSCREEN)
SA_Icon = pygame.image.load('./Assets/icon.png')
pygame.display.set_icon(SA_Icon)
pygame.display.set_caption("Shark Attack")
# Create the player
player = Player()

# Create all the levels
level_list = [levels.Level_01(player)]

# Set the current level
current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player.level = current_level
active_sprite_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


def text(font, text, size, x, y):
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    display.blit(text_surface, text_rect)


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()

    # Update the player.
    active_sprite_list.update()

    # Update items in the level
    current_level.update()

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    current_level.draw(screen)
    active_sprite_list.draw(screen)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
pygame.quit()

if __name__ == "__main__":
    main().game()
