from player import player_card as pc
import universal.game_board as gb
import fields.fcontainer as fc
import universal.side_bar as sb
import pygame
import math
import rules.rule_ui as r_ui

class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.balance = 1500.00
        self.money_spent_round = False
        self.round_complete = False
        self.position = pygame.Vector2(835, 575)
        self.win_condition = []
        self.task = []
        self.fid = 0 # Starting point
        self.properties = [] 
        self.jailStatus = False
        self.jailTurns = 0
        self.jailCard = False
        self.drunkStatus = 0
        self.successful_trade = False
        
    def spawn(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, 20)
        
    def move_to(self, screen, turns, board, field, dices, players, steps=5, hop_height=30):
        """Move the player to a new position with a hopping animation."""
        target_position = pygame.Vector2(field.x + 50, field.y + 50)
        start_position = self.position
        distance = target_position - start_position
        step_vector = distance / steps

        for step in range(steps):
            self.position += step_vector
            board(screen,turns,dices)
            
            # Draw all players, including the moving player and the others
            for player in players.values():
                if player == self:
                    hop = math.sin(math.pi * step / steps) * hop_height
                    hop_position = pygame.Vector2(self.position.x, self.position.y - hop)
                    pygame.draw.circle(screen, player.colour, hop_position, 20)
                else:
                    player.spawn(screen)
            
            # Draw the player at the new position with the hop
            pygame.draw.circle(screen, self.colour, hop_position, 20)
            pygame.display.flip()
            pygame.time.delay(30)
            
        self.position = target_position
        pygame.display.flip()
    
