class Property:
    def __init__(self, price: int, rent: float, owner):
        self.price = price
        self.rent = rent
        self.owner = owner
        self.is_mortgaged: bool = False  
        
    def change_owner(self, new_owner):
        self.owner = new_owner
        
    def mortgage_property(self, player):
        if not self.is_mortgaged:
            player.balance += self.price // 2
            self.is_mortgaged = True
        else:
            raise ValueError("Property is already mortgaged")
        
