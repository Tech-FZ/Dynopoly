import pygame
import universal.fonts as fonts
    
def ruleCard(screen):
    card_width = int(screen.get_width() / 4)
    card_x = (screen.get_width() / 4) * 3  # x position for the card
    card_y = 450  # y position for the card
    card_height = 150
    
    pygame.draw.rect(screen, "white", pygame.Rect(card_x, card_y, card_width, card_height))
    win_card_header = fonts.default_font.render("Rules", False, "black")
    header_location = pygame.Vector2(card_x+90, card_y-45)
    screen.blit(win_card_header, header_location)