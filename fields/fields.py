import pygame
import universal.fonts as fonts

def field_placement(screen, x, y):
    pygame.draw.rect(screen, "white", pygame.Rect(x, y, 125, 125))