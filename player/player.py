from items.property import Property
from player import player_card as pc
import universal.game_board as gb
import fields.fcontainer as fc
import rules.rule_ui as r_ui
import pygame
import math

class Player:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.balance = 1500.00
        self.position = pygame.Vector2(835, 575)
        self.ability = {}
        self.win_condition = []
        self.task = []
        self.fid = 0 # Starting point
        self.properties = []  # Changed to plural for clarity
        self.jailStatus = {'in_jail':False, "jail_turn":0, "has_jail_card":False}
        
    def spawn(self, screen):
        """Draw the player's token on the screen."""
        pygame.draw.circle(screen, self.colour, self.position, 20)
        
    def move_to(self, screen, field, dices, players, steps=5, hop_height=30):
        """Move the player to a new position with a hopping animation."""
        target_position = pygame.Vector2(field.x + 50, field.y + 50)
        start_position = self.position

        # Calculate the difference between the start and target positions
        distance = target_position - start_position
        step_vector = distance / steps

        for step in range(steps):
            # Move the player closer to the target position
            self.position += step_vector

            # Apply a hopping effect by adjusting the y-coordinate
            # Using a sine wave to simulate the hop
            # hop = math.sin(math.pi * step / steps) * hop_height
            # hop_position = pygame.Vector2(self.position.x, self.position.y - hop)

            # Clear the screen (or redraw the background)
            screen.fill("purple")
            r_ui.rule_ui_setup(screen)
            pc.player_card(screen,self)
            pc.win_condition_Card(screen, self)
            for fld in fc.f_container:
                fld.field_placement(screen)
            dices[0].spawnDice(screen)
            dices[1].spawnDice(screen)
            
            # Draw all players, including the moving player and the others
            for player in players.values():
                if player == self:
                    # Draw the moving player with the hop effect
                    hop = math.sin(math.pi * step / steps) * hop_height
                    hop_position = pygame.Vector2(self.position.x, self.position.y - hop)
                    pygame.draw.circle(screen, player.colour, hop_position, 20)
                else:
                    # Draw the non-moving player
                    player.spawn(screen)
            
            # Draw the player at the new position with the hop
            pygame.draw.circle(screen, self.colour, hop_position, 20)
            
            # Update the display
            pygame.display.flip()
            
            # Add a small delay for smoother animation
            pygame.time.delay(30)
            
        # Set the player's final position to the target
        self.position = target_position
        self.spawn(screen)  # Draw the player at the final position
    
    def collect_rent(self, player: 'Player', property: Property):
        """Collect rent from another player."""
        player.balance -= property.rent
        self.balance += property.rent
