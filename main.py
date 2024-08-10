# Third-party libraries
import pygame

# Other code files
import rules.rule_ui as r_ui
import fields.fields as fields
import player.player as pl

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    r_ui.rule_ui_setup(screen)

    # Field rendering
    fields.field_placement(screen, 5, 5)
    fields.field_placement(screen, 135, 5)
    fields.field_placement(screen, 265, 5)
    fields.field_placement(screen, 395, 5)
    fields.field_placement(screen, 525, 5)
    fields.field_placement(screen, 655, 5)
    fields.field_placement(screen, 785, 5)

    fields.field_placement(screen, 5, 135)
    fields.field_placement(screen, 785, 135)

    fields.field_placement(screen, 5, 265)
    fields.field_placement(screen, 785, 265)

    fields.field_placement(screen, 5, 395)
    fields.field_placement(screen, 785, 395)

    fields.field_placement(screen, 5, 525)
    fields.field_placement(screen, 135, 525)
    fields.field_placement(screen, 265, 525)
    fields.field_placement(screen, 395, 525)
    fields.field_placement(screen, 525, 525)
    fields.field_placement(screen, 655, 525)
    fields.field_placement(screen, 785, 525)

    player1 = pl.Player()
    player1.spawn(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()