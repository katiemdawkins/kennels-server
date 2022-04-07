class Employee():
    def __init__(self, id, name, locationId, position):
        self.id = id
        self.name = name
        self.locationId = locationId
        self.position = position
        
new_employee = Employee(1, "Ned Nancy", 1, "manager")