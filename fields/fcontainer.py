import fields.fields as fields

f_container = []

def contain(screen, f_type, f_name, f_owner, f_price, f_rent, fx, fy):
    field = fields.Field()
    field.type = f_type
    field.name = f_name
    field.owner = f_owner
    field.price = f_price
    field.rent = f_rent
    field.field_placement(screen, fx, fy)
    f_container.append(field)