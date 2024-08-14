import fields.fields as fields
import random

f_container = []

def contain(f_type, f_name, f_owner, f_price, f_rent, fx, fy):
    field = fields.Field(fx, fy, f_owner)
    field.type = f_type
    field.name = f_name
    field.owner = f_owner
    field.price = f_price
    field.rent = f_rent
    f_container.append(field)
    
def genStInvest():
    selectable = [
        ["street", "Street"],
        ["investment", "Investment"]
    ]
    
    rdm_idx = random.randint(0, len(selectable) - 1)
    return selectable[rdm_idx]

def genRegularField(x, y, player):
    selectedType = genStInvest()
    contain(selectedType[0], selectedType[1], player, 60, 8, x, y)
    
def genBoard(screen):
    for fld in f_container:
        fld.field_placement(screen)