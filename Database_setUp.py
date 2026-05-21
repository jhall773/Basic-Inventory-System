import sqlite3

conn = sqlite3.connect("inventory.db")

def main():
    cursor = conn.cursor()
    sql_str="""CREATE TABLE IF NOT EXISTS inventory (
            item TEXT NOT NULL PRIMARY KEY,
            quantity INTEGER)"""
    cursor.execute(sql_str)

    sql_str2="INSERT INTO inventory (item, quantity) VALUES ('Water bottle Packs', 100)"
    sql_str3="INSERT INTO inventory (item, quantity) VALUES ('Toilet Paper', 500)"
    sql_str4="INSERT INTO inventory (item, quantity) VALUES ('Paper Towel Rolls', 325)"
    sql_str5='INSERT INTO inventory (item, quantity) VALUES ("Women\'s Shirts", 100)'
    sql_str6='INSERT INTO inventory (item, quantity) VALUES ("Men\'s Shirts", 75)'
    sql_str7="INSERT INTO inventory (item, quantity) VALUES ('Bicycles', 150)"
    sql_str8="INSERT INTO inventory (item, quantity) VALUES ('Shoes', 245)"

    cursor.execute(sql_str2)
    cursor.execute(sql_str3)
    cursor.execute(sql_str4)
    cursor.execute(sql_str5)
    cursor.execute(sql_str6)
    cursor.execute(sql_str7)
    cursor.execute(sql_str8)

    conn.commit() # Nothing writes until you call this.
    cursor.close()


# This function returns the dictionary so you can easily tell what things were added/taken/changed with it.
def retrieve_db_data_as_dict():
    cur = conn.cursor()
    sql= "SELECT * FROM inventory" # Gets every (unique) key-value pair in the database.
    data = cur.execute(sql)
    data_dict = dict(data.fetchall()) # Triggers the retrieval of the data as a list of tuples, and dict() function turns it into a dictionary

    conn.commit()
    cur.close()
    return data_dict

# This function adds an item to the dictionary with the specified quantity
def add_to_db(item, quantity):
    cur = conn.cursor()
    sql= "INSERT INTO inventory (item, quantity) VALUES (?, ?)" # The "?" prevents SQL-injection attacks by seperating the SQL query structure from the data.
                                                                # Copiolot AI Assisted in this "?" string formatting.
    cur.execute(sql, (item, quantity))
    conn.commit()
    cur.close()

# This function updates an item that already exists in the dictionary with the specified quantity
def update_db(item, quantity):
    cur = conn.cursor()
    sql= "UPDATE inventory SET quantity = ? WHERE item = ?" # The "?" prevents SQL-injection attacks by seperating the SQL query structure from the data.
    cur.execute(sql, (quantity, item))
    conn.commit()
    cur.close()

def delete_from_db(item):
    cur = conn.cursor()
    sql= "DELETE FROM inventory WHERE item = ?" # The "?" prevents SQL-injection attacks by seperating the SQL query structure from the data.
    cur.execute(sql, (item,))
    conn.commit()
    cur.close()

if __name__=="__main__":
    main() # Only run the code to build the original DB if this script is run directly at it's the first time setting up the initial database.