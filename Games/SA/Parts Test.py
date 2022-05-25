import pygame
from player import Player
import levels

# Define some colors, you may want to add more
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
pygame.init()
# Set the width and height of the screen [width, height]
size = (pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1])
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("Test")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
player = Player()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_LEFT:
                player.go_left()
            if event.key == pygame.K_RIGHT:
                player.go_right()
            if event.key == pygame.K_UP:
                player.go_up()
            if event.key == pygame.K_DOWN:
                player.go_down()
    # --- Game logic should go here
    player.update()
    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    player.draw_player(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
