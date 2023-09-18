import sqlite3 

# https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
CONN = sqlite3.connect('lib/resources.db') 
# https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor
CURSOR = CONN.cursor()
 
class Pet:
    # ✅ 1. Add "__init__" with "name", "age", "species", "owner_id" and "id"
    def __init__(self, name, age, breed, owner_id=None, id=None):
        self.name = name 
        self.age = age 
        self.breed = breed 
        self.owner_id = owner_id 
        self.id = id 

    # ✅ 2. Create table
    @classmethod 
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS pets  
            (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                breed TEXT,
                owner_id INTEGER
            )
        """
        CURSOR.execute(sql)
        
    # ✅ 3. Drop table
    @classmethod
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS pets;
        """
        CURSOR.execute(sql)

    # ✅ 4. Insert instance into DB
    def save(self):
        # 🛑 TRY/EXCEPTS MAY BE VERY HELPFUL
        try: 
            sql = """ 
                INSERT INTO pets(name, age, breed, owner_id)
                VALUES (?, ?, ?, ?)
            """
            CURSOR.execute(sql, (self.name, self.age, self.breed, self.owner_id))
        except Exception as e:
            print(f'error: {e}')

    # ✅ 5. Initialize instance and insert into database
    @classmethod
    def create_and_save(cls, name, age, breed, owner_id):
        #1. create an instance of Pet 
        pet = cls(name, age, breed, owner_id)
        #2. insert said instance into the database
        pet.save()

    # ✅ 6. Create instance from DB, thus getting the ID
    # helper function for turning rows taken from databases into Pet instance's (that therefore, will have the database's ID)
    @classmethod
    def create_instance(cls, row):
        pet =  cls(
            id = row[0], #this is where we get the id from the database
            name = row[1],
            age = row[2],
            breed = row[3], 
            owner_id = row[4]
        )
        return pet 
 
    # ✅ 7. Get all rows
    @classmethod 
    def get_all(cls):
        sql = """ 
            SELECT * FROM pets; 
        """
        pet_array =[cls.create_instance(row) for row in CURSOR.execute(sql).fetchall()]
        return pet_array


    # ✅ 8. Get row by name
    @classmethod
    def find_by_name(cls, name):
        sql = """ 
            SELECT * FROM pets WHERE name=?;
        """
        row = CURSOR.execute(sql, (name, )).fetchone()
        if not row: 
            return None 
        else: 
            return Pet.create_instance(row)

    # ✅ 9. Get row by id
    @classmethod 
    def find_by_id(cls, id):
        sql = """ 
            SELECT * FROM pets WHERE id=?;
        """
        row = CURSOR.execute(sql, (id, )).fetchone()
        if not row:
            return None
        else:
            #return cls.create_instance(row)
            return Pet.create_instance(row)

    # ✅ 10. Find row, otherwise create row
    @classmethod
    def find_or_create(cls, name=None, age=None, breed=None):
        # 🛑 matching for owner_id when owner_id is None / Null was causing issues
        # ✅ 10a. Search for pet
        sql = """ 
            SELECT * FROM pets WHERE (name, age, breed) = (?, ?, ?);
        """
        row = CURSOR.execute(sql, (name, age, breed)).fetchone()
        # ✅ 10b. Insert pet if it does not exist
        if not row: 
            # sql = """ 
            #     INSERT INTO pets(name, age, breed, owner_id) VALUES (?, ?, ?, ?);
            # """
            Pet.create_and_save(name, age, breed, None)
            return cls.find_by_id(CURSOR.lastrowid)
        # ✅ 10c. Return pet if it does exist
        else: 
            return cls.create_instance(row)

    # ✅ 11. Update row
    # edit an instance's attribute, and then call update() to insert that new attribute into the database
    def update(self):
        sql = """ 
            UPDATE pets SET name = ?, age = ?, breed = ?, owner_id = ? WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.breed, self.owner_id, self.id))

    # ✅ Delete row
    @classmethod 
    def delete(cls, id):
        sql = """ 
            DELETE FROM pets WHERE id=?; 
        """
        CURSOR.execute(sql, (id, ))

    @classmethod 
    def delete_by_name(cls, name):
        sql = """ 
            DELETE FROM pets WHERE name = ?;
        """
        CURSOR.execute(sql, (name, ))
    

    def __repr__(self):
        return f'<{self.id}. Pet {self.name} is a {self.age} yr old {self.breed} >'