class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, species, location_id, customer_id, status):
        self.id = id
        self.name = name
        self.species = species
        self.location_id = location_id
        self.customer_id = customer_id
        self.status = status
        
new_animal = Animal(1, "Snickers", "Dog", 1, 4, "Recreation")