import pygame
import random

import universal.fonts as fonts

class Dice:
    def __init__(self):
        self.value = 1
        self.x = 145
        self.y = 480

    def updateDice(self, screen):
        dice_lbl = fonts.default_font.render(str(self.value), False, (0, 0, 0))
        screen.blit(dice_lbl, pygame.Vector2(self.x + 8, self.y))

    def rollDice(self, screen):
        self.value = random.randint(1, 6)
        self.updateDice(screen)
        
    def spawnDice(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, 25, 25))
        self.updateDice(screen)