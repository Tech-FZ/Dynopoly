from player.player import Player

class Investment:
    def __init__(self, owner: Player, amount: float = 100, interest: float = 0.1):
        self.amount = amount
        self.interest = interest
        self.owner = owner
        
    def update_amount(self, amount: float):
        self.amount += amount
        
    def earn_interest(self):
        self.amount += self.amount * self.interest
        
    def change_owner(self,player):
        self.owner = player
    
    def sell_investment(self):
        self.owner = None
