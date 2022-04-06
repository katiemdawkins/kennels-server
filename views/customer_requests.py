CUSTOMERS = [
    {
        "id": 1,
        "name": "Anais McKenzie",
    },
     {
        "id": 2,
        "name": "Leon Cartwright",
    },
      {
        "id": 3,
        "name": "Renee Koss Sr.",
    },
       {
        "id": 4,
        "name": "Lynne Zboncak",
    },
        {
        "id": 5,
        "name": "Bobby Grant",
    },
         {
        "id": 6,
        "name": "Essie Koch",
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