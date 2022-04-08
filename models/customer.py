class Customer():
    
    def __init__(self, id, name, address, email, password):
        self.id = id
        self.name = name
        self.address = address
        self.email = email
        self.password = password
        
new_customer = Customer(1, "Anais McKenzie", "555 Street", "anais@email.com", "12345")