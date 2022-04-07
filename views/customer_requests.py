from sqlite3 import Cursor


CUSTOMERS = [
    {
        "id": 1,
        "name": "Anais McKenzie",
        "status": "adopter"
    },
     {
        "id": 2,
        "name": "Leon Cartwright",
        "status": "adopter"
    },
      {
        "id": 3,
        "name": "Renee Koss Sr.",
        "status": "foster"
    },
       {
        "id": 4,
        "name": "Lynne Zboncak",
        "status": "foster"
    },
        {
        "id": 5,
        "name": "Bobby Grant",
        "status": "volunteer"
    },
         {
        "id": 6,
        "name": "Essie Koch",
        "status": "volunteer"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None
    
    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer
    
    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]
    
    new_id = max_id +1
    
    customer["id"] = new_id
    
    CUSTOMERS.append(customer)
    
    return(customer)

def delete_customer(id):
    customer_index = -1
    
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index
        
        if customer_index >= 0:
            CUSTOMERS.pop(customer_index)
            
def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break