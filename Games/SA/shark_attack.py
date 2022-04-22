import pygame
import constants

# Define some colors, you may want to add more
pygame.init()
# Set the width and height of the screen [width, height]
DISPLAY_W, DISPLAY_H = pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1]
display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H), pygame.FULLSCREEN)
pygame.display.set_caption("Shark Attack")
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    x, y = display.get_size()
    mid_w, mid_h = x / 2, y / 2
    # --- All events are detected here
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here.
    #  Here, we clear the screen to white.
    background = pygame.image.load("./Assets/Water-BG.jpeg")
    background = pygame.transform.scale(background, (DISPLAY_W, DISPLAY_H))
    display.blit(background, (0, 0))

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
