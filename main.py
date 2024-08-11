# Third-party libraries
import pygame

# Other code files
import rules.rule_ui as r_ui
import fields.fields as fields
import fields.fcontainer as fc
import player.player as pl
import player.player_card as pc
import dice.dice as dc
import universal.button as btn

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player1 = pl.Player("Nicolas")

dc1 = dc.Dice()

dc2 = dc.Dice()
dc2.x = 175

y = 525
x = 785

while x >= 5:
    if x == 785 and y == 525:
        fc.contain(screen, "start", "Start", "None", 200, 0, x, y)

    elif x == 785 and y == 5:
        fc.contain(screen, "gotojail", "Go to jail", "None", 0, 0, x, y)

    else:
        fc.contain(screen, "street", "Street", "Bank", 60, 8, x, y)

    x -= 130

y -= 130
x = 5

while y >= 5:
    if x == 5 and y == 5:
        fc.contain(screen, "freeparking", "Free parking", "None", 0, 0, x, y)

    elif x == 785 and y == 5:
        fc.contain(screen, "gotojail", "Go to jail", "None", 0, 0, x, y)

    else:
        fc.contain(screen, "street", "Street", "Bank", 60, 8, x, y)

    y -= 130

y = 5
x += 130

while x <= 785:
    if x == 785 and y == 5:
        fc.contain(screen, "gotojail", "Go to jail", "None", 0, 0, x, y)
        
    else:
        fc.contain(screen, "street", "Street", "Bank", 60, 8, x, y)

    x += 130

x = 785
y += 130

while y <= 395:
    if x == 785 and y == 5:
        fc.contain(screen, "gotojail", "Go to jail", "None", 0, 0, x, y)

    else:
        fc.contain(screen, "street", "Street", "Bank", 60, 8, x, y)
        
    y += 130

def rollDices():
    dc1.rollDice(screen)
    dc2.rollDice(screen)

    total_value = dc1.value + dc2.value

    new_fid = player1.fid + total_value
    
    if new_fid > len(fc.f_container):
        new_fid = 0 + (new_fid - len(fc.f_container))
        
    player1.fid = new_fid

    player1.move_to(screen, fc.f_container[player1.fid])


# insert buttons here
rodi_btn = btn.Button(
    screen,
    "Roll dice",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    205,
    480,
    65,
    25,
    rollDices,
)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        rodi_btn.checkClick(event)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    r_ui.rule_ui_setup(screen)
    
    for fld in fc.f_container:
        fld.field_placement(screen)

    """ while y <= 525:
        x = 5

        while x <= 785:
            if x == 5 and y == 5:
                fc.contain(screen, "freeparking", "Free parking", "None", 0, 0, x, y)
            
            elif x == 785 and y == 5:
                fc.contain(screen, "gotojail", "Go to jail", "None", 0, 0, x, y)

            elif x == 5 and y == 525:
                fc.contain(screen, "jail", "Jail", "None", 50, 0, x, y)

            elif x == 785 and y == 525:
                fc.contain(screen, "start", "Start", "None", 200, 0, x, y)

            else:
                if y == 5 or y == 525 or x == 5 or x == 785:
                    fc.contain(screen, "street", "Street", "Bank", 60, 8, x, y)

            x += 130

        y += 130 """

    player1.spawn(screen)
    
    pc.player_card(screen, player1)

    dc1.spawnDice(screen)
    dc2.spawnDice(screen)

    rodi_btn.updateButton(rodi_btn.bg_colour, rodi_btn.txt_colour)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
