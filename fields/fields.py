import pygame
import universal.fonts as fonts
from player.player import Player

class Field:
    def __init__(self, x, y, player:Player):
        self.type = "street"
        self.name = "Street"
        self.owner = player
        self.price = 60
        self.rent = [8, 20, 35, 50, 65, 100]
        self.players = []
        self.houseCount = 0
        self.hotelAvailable = False
        self.x = x
        self.y = y

    def field_placement(self, screen):
        field_lbl_pos = pygame.Vector2(self.x + 10, self.y + 10)
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, 125, 125))

        field_lbl = fonts.default_font.render(self.name, False, (0, 0, 0))
        screen.blit(field_lbl, field_lbl_pos)
        
        owner_lbl_pos = pygame.Vector2(self.x + 10, self.y + 100)
        if self.owner is not None:
            owner_lbl = fonts.default_font.render(self.owner.name, False, (0,0,0))
        else:
            owner_lbl = fonts.default_font.render(f"{self.owner}", False, (0,0,0))
        screen.blit(owner_lbl, owner_lbl_pos)

    