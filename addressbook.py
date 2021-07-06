claude = [{"name": "Claude Shannon", "street": "5 Cambridge St", "city": "Winchester", "state": "MA", "zip": "01890", "phone": "555-1212", "email": "bitplayer@mit.com"},
 {"name": "Charlie Brown", "street": "5 Cambridge St", "city": "Winchester", "state": "MA", "zip": "01890", "phone": "555-1212", "email": "charliebrown@mit.com"}, 
 {"name": "Bruce Wayne", "street": "5 Cambridge St", "city": "Winchester", "state": "MA", "zip": "01890", "phone": "555-1212", "email": "brucewayne@mit.com"}, 
 {"name": "Clark Kent", "street": "5 Cambridge St", "city": "Winchester", "state": "MA", "zip": "01890", "phone": "555-1212", "email": "clarkkent@mit.com"}, 
 {"name": "Jose Andres", "street": "5 Cambridge St", "city": "Winchester", "state": "MA", "zip": "01890", "phone": "555-1212", "email": "joseandres@mit.com"}]

choice = input("Enter a name: ")

for item in claude:
    if item["name"] == choice:
        print(item["email"])