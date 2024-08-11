import pygame
import universal.fonts as fonts

class Button:
    def __init__(self, screen, txt, bg_colour, txt_colour, bgc_hover, txtc_hover, x, y, width, height, ftc=None):
        self.screen = screen
        self.ftc = ftc
        self.txt = txt
        self.bg_colour = bg_colour
        self.txt_colour = txt_colour
        self.bgc_hover = bgc_hover
        self.txtc_hover = txtc_hover
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def updateButton(self, bgc, txtc):
        pygame.draw.rect(self.screen, bgc, self.rect)
        btn_lbl = fonts.default_font.render(str(self.txt), False, txtc)
        self.screen.blit(btn_lbl, pygame.Vector2(self.x, self.y))

    def checkClick(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            if self.rect.collidepoint(event.pos):
                print(f"Mouse clicked at: {event.pos}")
                if self.ftc:
                    self.ftc()