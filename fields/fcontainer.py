import fields.fields as fields
import random

f_container = []

def contain(f_type, f_name, f_owner, f_price, f_rent, fx, fy):
    field = fields.Field(fx, fy)
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

def genRegularField(x, y):
    selectedType = genStInvest()
    contain(selectedType[0], selectedType[1], "Bank", 60, 8, x, y)