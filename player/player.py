import pygame

class Player:
    def __init__(self):
        self.balance = 1500
        self.position = pygame.Vector2(848, 588)

    def spawn(self, screen):
        pygame.draw.circle(screen, "red", self.position, 20)