import pygame
import universal.fonts as fonts

class Field:
    def __init__(self, x, y):
        self.type = "street"
        self.name = "Street"
        self.owner = "Bank"
        self.price = 60
        self.rent = 8
        self.players = []
        self.houseCount = 0
        self.hotelAvailable = False
        self.x = x
        self.y = y

    def field_placement(self, screen, x, y):
        field_lbl_pos = pygame.Vector2(self.x + 10, self.y + 10)
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, 125, 125))

        field_lbl = fonts.default_font.render(self.name, False, (0, 0, 0))
        screen.blit(field_lbl, field_lbl_pos)

    