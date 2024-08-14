import pygame
import universal.fonts as fonts
import rules.rule_algo as r_algo

latest_event = ""
    
def ruleCard(screen):
    global latest_event
    card_width = int(screen.get_width() / 4)
    card_x = (screen.get_width() / 4) * 3  # x position for the card
    card_y = 450  # y position for the card
    card_height = 150
    
    pygame.draw.rect(screen, "white", pygame.Rect(card_x, card_y, card_width, card_height))
    win_card_header = fonts.default_font.render("Rules", False, "black")
    header_location = pygame.Vector2(card_x+90, card_y-45)
    screen.blit(win_card_header, header_location)
    
    house_pr_lbl = fonts.default_font.render(f"House Price: {r_algo.house_price}", False, "black")
    hotel_pr_lbl = fonts.default_font.render(f"Hotel Price: {r_algo.hotel_price}", False, "black")
    fp_lbl = fonts.default_font.render(f"Free Parking: {r_algo.free_parking}", False, "black")
    lat_ev_lbl = fonts.small_font.render(latest_event, False, "black")
    
    house_pr_loc = pygame.Vector2(card_x + 10, card_y + 10)
    hotel_pr_loc = pygame.Vector2(card_x + 10, card_y + 40)
    fp_loc = pygame.Vector2(card_x + 10, card_y + 70)
    lat_ev_loc = pygame.Vector2(card_x + 10, card_y + 100)
    
    screen.blit(house_pr_lbl, house_pr_loc)
    screen.blit(hotel_pr_lbl, hotel_pr_loc)
    screen.blit(fp_lbl, fp_loc)
    screen.blit(lat_ev_lbl, lat_ev_loc)