import pygame
import universal.button as btn
import universal.fonts as fonts

def reject_ftc():
    pass

def offer_card(screen, phase, ftc, kw_args = None):
    accept = btn.Button(
    screen,
    "Yes",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    ((screen.get_width() / 4)  + 65),
    (screen.get_height()/2+100),
    65,
    25,
    ftc,
    kw_args=kw_args
)
    
    reject = btn.Button(
    screen,
    "No",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    ((screen.get_width() / 4)  + 140),
    (screen.get_height()/2+100),
    65,
    25,
)
    
    
    oc_width = int(screen.get_width() / 5)
    oc_location = pygame.Vector2((screen.get_width() / 4)  + 50, screen.get_height()/2)
    
    pygame.draw.rect(screen, "gray", pygame.Rect(((screen.get_width() / 4),  screen.get_height()/2, oc_width,150)))

    oc_header = fonts.default_font.render("Would you like to buy?", False, (0, 0, 0))
    screen.blit(oc_header, oc_location)
    accept.updateButton(accept.bg_colour, accept.txt_colour)
    reject.updateButton(reject.bg_colour, reject.txt_colour)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            accept.checkClick(event)
            reject.checkClick(event)
            phase = not phase
    
    pygame.display.flip()
    
    return phase

def house_hotel_card(screen, phase, ftc_house, ftc_hotel, kw_args = None):
    house = btn.Button(
    screen,
    "House",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    ((screen.get_width() / 4)  + 20),
    (screen.get_height()/2+100),
    65,
    25,
    ftc_house,
    kw_args=kw_args
)
    
    hotel = btn.Button(
    screen,
    "Hotel",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    ((screen.get_width() / 4)  + 100),
    (screen.get_height()/2+100),
    65,
    25,
    ftc_hotel,
    kw_args=kw_args
)
    
    reject = btn.Button(
    screen,
    "No",
    (255, 255, 255),
    (0, 0, 0),
    (5, 5, 5),
    (0, 0, 0),
    ((screen.get_width() / 4)  + 180),
    (screen.get_height()/2+100),
    65,
    25,
)
    
    
    oc_width = int(screen.get_width() / 5)
    oc_location1 = pygame.Vector2((screen.get_width() / 4)  + 50, screen.get_height()/2)
    oc_location2 = pygame.Vector2((screen.get_width() / 4)  + 50, screen.get_height()/2 + 30)
    
    pygame.draw.rect(screen, "gray", pygame.Rect(((screen.get_width() / 4),  screen.get_height()/2, oc_width,150)))

    oc_header1 = fonts.default_font.render("Would you like to buy", False, (0, 0, 0))
    oc_header1 = fonts.default_font.render("Would you like to buy", False, (0, 0, 0))
    screen.blit(oc_header1, oc_location1)
    house.updateButton(house.bg_colour, house.txt_colour)
    hotel.updateButton(hotel.bg_colour, hotel.txt_colour)
    reject.updateButton(reject.bg_colour, reject.txt_colour)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            house.checkClick(event)
            hotel.checkClick(event)
            reject.checkClick(event)
            phase = not phase
    
    pygame.display.flip()
    
    return phase