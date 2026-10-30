
# pygame template

import pygame

pygame.init()

WIDTH = 800
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

suncircle_x = WIDTH / 2
suncircle_y = 100
mooncircle_x = WIDTH
mooncircle_y = HEIGHT

sky = 1

# ---------------------------

running = True
while running:

    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # GAME STATE UPDATES

    # moon movement aligning path towards sun
    mooncircle_x -= 1.0
    mooncircle_y -= 1.5

    # sky changes color (abs means absolute value so that it doesnt calculate a negative value)
    distance = abs(mooncircle_x - suncircle_x)
#   min means whichever number is smaller so the smaller number is assigned to sky
    if mooncircle_x >= 100:
        sky = min(1.0, distance / 200)
    else:
        sky = 0

    # drawing
    screen.fill((135 * sky, 206 * sky, 235 * sky))

    # sun
    pygame.draw.circle(screen, (255, 223, 34), (int(suncircle_x), int(suncircle_y)), 80)

    # moon
    pygame.draw.circle(screen, (20, 10, 10), (int(mooncircle_x), int(mooncircle_y)), 81)

    # building
    pygame.draw.rect(screen, (40, 40, 50), (250, 350, 300, 350))

    # windows light up during eclipse
    if distance <= 90:
        pygame.draw.rect(screen, (255, 220, 100), (290, 390, 50, 60))
        pygame.draw.rect(screen, (255, 220, 100), (460, 390, 50, 60))

        pygame.draw.rect(screen, (255, 220, 100), (290, 490, 50, 60))
        pygame.draw.rect(screen, (255, 220, 100), (460, 490, 50, 60))

        pygame.draw.rect(screen, (255, 220, 100), (290, 590, 50, 60))
        pygame.draw.rect(screen, (255, 220, 100), (460, 590, 50, 60))
    elif sky == 0:
            pygame.draw.rect(screen, (255, 220, 100), (290, 390, 50, 60))
            pygame.draw.rect(screen, (255, 220, 100), (460, 390, 50, 60))
    
            pygame.draw.rect(screen, (255, 220, 100), (290, 490, 50, 60))
            pygame.draw.rect(screen, (255, 220, 100), (460, 490, 50, 60))
    
            pygame.draw.rect(screen, (255, 220, 100), (290, 590, 50, 60))
            pygame.draw.rect(screen, (255, 220, 100), (460, 590, 50, 60))

    # ---------------------------
    # sun turns into a pumpkin after the eclipse

    if mooncircle_x < 100:

        # orange pumpkin
        pygame.draw.circle(screen, (255, 120, 0), (400, 100), 80)

        # pumpkin leaf or stem whatever
        pygame.draw.rect(screen, (40, 120, 30), (390, 10, 20, 25))

        # eye left
        pygame.draw.polygon(screen, (0, 0, 0), [(350, 75), (380, 75), (365, 105)])

        # eye right
        pygame.draw.polygon(screen, (0, 0, 0), [(400, 75), (430, 75), (415, 105)])

        # mouth
        pygame.draw.rect(screen, (0, 0, 0), (365, 125, 90, 15))

    # ---------------------------

    # must be the last two lines of the game loop
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
