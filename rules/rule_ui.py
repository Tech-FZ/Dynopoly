import pygame
import universal.fonts as fonts

# This is just the sidebar. It has been moved to the universal folder in a separate branch and is to be removed from the main branch
# in case GitHub merges this function into it. - Nicolas Lucien/lucien-rowan/Tech-FZ
def rule_ui_setup(screen):
    rule_ui_width = int(screen.get_width() / 4)
    rule_ui_location = pygame.Vector2((screen.get_width() / 4) * 3 + 50, 10)
    
    pygame.draw.rect(screen, "gray", pygame.Rect((screen.get_width() / 4) * 3, 0, rule_ui_width, screen.get_height()))

    r_header = fonts.default_font.render("Misonic Project", False, (0, 0, 0))
    screen.blit(r_header, rule_ui_location)
    
def ruleCard(screen):
    card_width = int(screen.get_width() / 4)
    card_x = (screen.get_width() / 4) * 3  # x position for the card
    card_y = 450  # y position for the card
    card_height = 150
    
    pygame.draw.rect(screen, "white", pygame.Rect(card_x, card_y, card_width, card_height))
    win_card_header = fonts.default_font.render("Rules", False, "black")
    header_location = pygame.Vector2(card_x+90, card_y-45)
    screen.blit(win_card_header, header_location)