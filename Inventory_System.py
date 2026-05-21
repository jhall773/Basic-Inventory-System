from Database_setUp import retrieve_db_data_as_dict
from Database_setUp import add_to_db
from Database_setUp import update_db
from Database_setUp import delete_from_db

def get_inventory_dict():
    print(retrieve_db_data_as_dict())
    print() # Print a newline space after showing the dictionary

def display_items(sort_preference):
    item_names = []
    item_quantities = []
    inventory_items = retrieve_db_data_as_dict()
    for item, quantity in inventory_items.items():
        item_names.append(item)
        item_quantities.append(quantity)

    # Sort by Name
    if sort_preference == 1:
        for item in sorted(item_names):
            print(f"Item: {item:<40} Quantity: {str(inventory_items[item])}") # The ':<40' in the string left aligns in a 40 char wide column, so all the quanities line up after.
                                                                              # Copiolot AI assisted in this ':<40' string formatting.
    # Sort by quantity
    if sort_preference == 2:
        for quantity in sorted(item_quantities):
            for item in inventory_items.keys():
                if(inventory_items[item] == quantity):
                    print(f"Item: {item:<40} Quantity: {str(inventory_items[item])}")
    
    print() # Print a newline space after showing the sorted dictionary

def add_item(item, quantity):
    if item not in retrieve_db_data_as_dict():
        add_to_db(item, quantity)
        get_inventory_dict() # Prints the results of the new dictionary after you add an item to it.
    else:
        print("Sorry, this item is already in the inventory system. Please use the '2. update stock' (or '3. delete item') option instead.")

def update_item(item, quantity):
    if item in retrieve_db_data_as_dict():
        update_db(item, quantity)
        get_inventory_dict() # Prints the results of the new dictionary after you update an item's quantity.
    else:
        print("Sorry, this item is not in the inventory system. Please use the '1. add item' option instead.")

def delete_item(item):
    if item in retrieve_db_data_as_dict():
        delete_from_db(item)
        get_inventory_dict() # Prints the results of the new dictionary after delete an item from the inventory list.



# This is where the system actually handles requests from the users.
print("Hello, you have just entered into the inventory system.\nPlease enter in a number to select one of the options below:\n")
userIn = ""

while(userIn != 5):
    # After you add/update/delete/or display inventory data, make another choice and repeat the process until you quit (by pressing 5) 
    userIn = input("1. add item\n2. update stock\n3. delete item\n4. display all items\n5. quit\n")

    while (userIn.isdigit() == False) or (int(userIn) != 1) and (int(userIn) != 2) and (int(userIn) != 3) and (int(userIn) !=4) and (int(userIn) != 5):
        print("Sorry, that it not a valid option for this system. Please enter the number of a valid option.\n")
        userIn = input("1. add item\n2. update stock\n3. delete item\n4. display all items\n5. quit\n")

    # Performing Operations Based on User's Options
    userIn = int(userIn)
    if userIn == 1: # Adding an Item
        item = input("Please enter the name of the item to add to the database: ")
        qty = input("Please enter the quantity of the item: ")
        while qty.isnumeric() == False or int(qty) <= 0:
            input("I'm sorry, that is not a valid quanity for this system. Please use a number greater than 0.\n")
            qty = input("Please enter the quantity of the item: ")
        add_item(item, int(qty))

    if userIn == 2: # Updating an Item
        item = input("Please enter the name of the item to update in the database: ")
        qty = input("Please enter the quantity of the item: ")
        while qty.isnumeric() == False or int(qty) < 0:
            input("I'm sorry, that is not a valid quanity for this system. Please use a positive number.\n")
            qty = input("Please enter the quantity of the item: ")
        update_item(item, int(qty))

    if userIn == 3: # Deleting an Item
        item = input("Please enter the name of the item to delete in the database: ")
        delete_item(item)

    if userIn == 4: # Displaying all Items
        sort = input("Would you like to see the display of inventory items ordered by Name or by Quantity?\nPlease enter the number 1 for Name or 2 for Quantity: ")
        while sort.isdigit() == False or int(sort) not in (1,2):
            sort = input("I'm sorry, that is not a valid choice for this system.\nPlease enter the number 1 (to order items by Name) or 2 (to order items by Quantity): ")
        display_items(int(sort))
    
    # Write code to backtrack in case the 'delete' selection was unintentional.
    # Run a Test adding a cereal boxes item / updating it / deleting it / (showing the results of each step with option 4 / and then quiting.
print("Closing inventory system application...")



    
    



