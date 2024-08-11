from items.property import Property
import pygame

class Player:
    def __init__(self):
        self.balance = 1500.00
        self.position = pygame.Vector2(848, 588)
        self.ability = {}
        self.win_condition = []
        self.task = []
        self.properties = []  # Changed to plural for clarity
        
    def spawn(self, screen):
        """Draw the player's token on the screen."""
        pygame.draw.circle(screen, "red", self.position, 20)
        
    def move_to(self, screen, field):
        """Move the player to a new position and redraw them."""
        self.position = pygame.Vector2(field.x, field.y)
        self.spawn(screen)
    
    def collect_rent(self, player: 'Player', property: Property):
        """Collect rent from another player."""
        player.balance -= property.rent
        self.balance += property.rent
