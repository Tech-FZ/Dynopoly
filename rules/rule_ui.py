import pygame

def rule_ui_setup(screen):
    rule_ui_width = int(screen.get_width() / 4)
    rule_ui_location = pygame.Vector2((screen.get_width() / 4) * 3, 0)
    
    pygame.draw.rect(screen, "red", pygame.Rect((screen.get_width() / 4) * 3, 0, rule_ui_width, screen.get_height()))