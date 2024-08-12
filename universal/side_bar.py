import pygame
import universal.fonts as fonts

def sb_setup(screen):
    sb_width = int(screen.get_width() / 4)
    sb_location = pygame.Vector2((screen.get_width() / 4) * 3 + 50, 10)
    
    pygame.draw.rect(screen, "gray", pygame.Rect((screen.get_width() / 4) * 3, 0, sb_width, screen.get_height()))

    r_header = fonts.default_font.render("Misonic Project", False, (0, 0, 0))
    screen.blit(r_header, sb_location)