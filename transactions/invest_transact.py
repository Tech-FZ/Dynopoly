def invest(player, investment):
    if player.balance >= investment.price:
        player.balance -= investment.price
        investment.owner = player
        
def earn_money(player, investment):
    player.balance -= investment.rent * 4
    investment.owner.balance += investment.rent