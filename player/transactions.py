from typing import List, Optional
from player.player import Player
from items.property import Property
from items.investment import Investment
from dataclasses import dataclass

@dataclass
class Transaction:
    buyer: Player
    seller: Player
    property: Optional[Property] = None
    investment: Optional[Investment] = None
    
    def buy_property(self):
        if self.property:
            self.property.owner = self.buyer
            self.seller.balance += self.property.price
            self.buyer.balance -= self.property.price
            
    def trade(self, trade_items: List[Optional[object]]):
        for item in trade_items:
            if isinstance(item, (Property, Investment)):
                item.owner = self.buyer
            elif isinstance(item, float):
                self.seller.balance -= item
                self.buyer.balance += item
