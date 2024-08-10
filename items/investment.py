from player.player import Player

class Investment:
    def __init__(self, amount: float, interest: float, owner: Player):
        self.amount = amount
        self.interest = interest
        self.owner = owner
        
    def update_amount(self, amount: float):
        self.amount += amount
        
    def earn_interest(self):
        self.amount += self.amount * self.interest
    
    def sell_investment(self):
        self.owner = None
