import sqlite3 

# https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
CONN = sqlite3.connect('lib/resources.db') 
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()
 
class Pet:
    pass 
    # ✅ 1. Add "__init__" with "name", "age", "species", "owner_id" and "id"

    # ✅ 2. Create table
        
    # ✅ 3. Drop table

    # ✅ 4. Insert instance into DB

    # ✅ 5. Initialize instance and insert into database

    # ✅ 6. Create instance from DB, thus getting the ID
 
    # ✅ 7. Get all rows

    # ✅ 8. Get row by name

    # ✅ 9. Get row by id

    # ✅ 10. Find row, otherwise create row
        # ✅ 10a. Search for pet
        # ✅ 10b. Insert pet if it does not exist
        # ✅ 10c. Return pet if it does exist

    # ✅ 11. Update row
