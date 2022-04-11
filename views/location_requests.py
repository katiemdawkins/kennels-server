import sqlite3
import json
from models import Location

LOCATIONS = [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "101 Penn Ave"
        }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None
    
    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location
    
    return requested_location

def create_location(location):
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)
    return(location)

def delete_location(id):
    location_index = -1
    
    for index,location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
        
        if location_index >=0:
            LOCATIONS.pop(location_index)
            
def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location ["id"] == id:
            LOCATIONS[index] = new_location
            break
        
def get_all_locations():
    with sqlite3.connect("./kennel.sqlite3") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)
        
        locations = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            
            location = Location(row['id'],row['name'], row['address'])
            locations.append(location.__dict__)
            
    return json.dumps(locations)

def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a  
        WHERE a.id = ?             
        """, (id,))
        
        data = db_cursor.fetchone()
        
        location = Location(data['id'], data['name'], data['address'])
        
        return json.dumps(location.__dict__)
    
# def get_customers_by_email(email):

#     with sqlite3.connect("./kennel.sqlite3") as conn:
#         conn.row_factory = sqlite3.Row
#         db_cursor = conn.cursor()

#         # Write the SQL query to get the information you want
#         db_cursor.execute("""
#         select
#             c.id,
#             c.name,
#             c.address,
#             c.email,
#             c.password
#         from Customer c
#         WHERE c.email = ?
#         """, ( email, ))

#         customers = []
#         dataset = db_cursor.fetchall()

#         for row in dataset:
#             customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
#             customers.append(customer.__dict__)

#     return json.dumps(customers)