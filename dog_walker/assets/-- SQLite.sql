-- SQLite
-- ✅ 1. Select specific columns

-- ✅ 2. Create new database structure
-- ✅ 2a. Remove owners table
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS procedures;
-- ✅ 2b. Create owners table
CREATE TABLE owners(
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
);
-- ✅ 2c. Create pets table
CREATE TABLE pets(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    breed TEXT,
    owner_id INTEGER,
        FOREIGN KEY(owner_id) REFERENCES owners(id)
);


-- procedure table for many to many 
CREATE TABLE procedures(
    id INTEGER PRIMARY KEY,
    name TEXT
);



-- appointment table for many to many
CREATE TABLE appointments(
    id INTEGER PRIMARY KEY,
    staff TEXT,
    pet_id INTEGER, 
    procedure_id INTEGER,
        FOREIGN KEY(pet_id) REFERENCES pets(id)
        FOREIGN KEY(procedure_id) REFERENCES procedures(id)
    );



-- ✅ 3. Modify pets table
-- ✅ 3a. Add image_url to pets
ALTER TABLE pets 
ADD COLUMN image_url TEXT;
-- ✅ 3b. Rename column

-- ✅ 4. Create new instances
-- ✅ 4a. Use chatGPT to create random owners
-- given a sql table owners with the following columns: name (text), email (text), phone (text) create 10 instances 
INSERT INTO owners (name, email, phone)
VALUES
  ('John Doe', 'john.doe@example.com', '1234567890'),
  ('Jane Smith', 'jane.smith@example.com', '9876543210'),
  ('Michael Johnson', 'michael.johnson@example.com', '5551234567'),
  ('Sarah Davis', 'sarah.davis@example.com', '7890123456'),
  ('David Lee', 'david.lee@example.com', '5557891234'),
  ('Emily Brown', 'emily.brown@example.com', '1237894561'),
  ('Chris Anderson', 'chris.anderson@example.com', '3214567890'),
  ('Jessica Miller', 'jessica.miller@example.com', '5557896543'),
  ('Ryan Wilson', 'ryan.wilson@example.com', '7893214567'),
  ('Laura Taylor', 'laura.taylor@example.com', '5559876543');

-- ✅ 4b. Use chat GPT to create sample data for pets
-- given an SQL table of pets generate 10 instances with attributes of name, age, breed also with a foreign key of 1-10 referencing owner(id)
INSERT INTO pets (name, age, breed, owner_id)
VALUES
  ('Fluffy', 3, 'Persian', 1),
  ('Buddy', 5, 'Labrador', 5),
  ('Whiskers', 2, 'Siamese', 3),
  ('Rex', 4, 'German Shepherd', 2),
  ('Mittens', 1, 'Maine Coon', 5),
  ('Charlie', 3, 'Golden Retriever', 8),
  ('Luna', 2, 'Ragdoll', 7),
  ('Rocky', 4, 'Bulldog', 1),
  ('Coco', 6, 'Poodle', 9),
  ('Oliver', 3, 'Bengal', 10);

INSERT INTO procedures (name)
VALUES
  ('Spaying'),
  ('Neutering'),
  ('Dental Cleaning'),
  ('Vaccinations'),
  ('Orthopedic Surgery');
INSERT INTO appointments (staff, pet_id, procedure_id)
VALUES
  ('Dr. Smith', 1, 3),
  ('Dr. Johnson', 2, 1),
  ('Dr. Davis', 10, 2),
  ('Dr. Anderson', 4, 4),
  ('Dr. Miller', 5, 5),
  ('Dr. Wilson', 6, 3),
  ('Dr. Taylor', 4, 1),
  ('Dr. Brown', 8, 2),
  ('Dr. Lee', 1, 4),
  ('Dr. Anderson', 10, 5);
-- ✅ 5. Read data
-- ✅ 5a. Get all columns from pets
SELECT * FROM pets;
SELECT id, name, breed FROM pets;
-- ✅ 5b. Select pet by name
SELECT * FROM pets WHERE name = "Coco";
-- ✅ 5d. Select pets by age 
SELECT * FROM pets WHERE age = 3;
SELECT * FROM pets WHERE age < 3;

-- ✅ 6. Update data
-- ✅ 6a. Update pet's age by name
UPDATE pets 
SET age = 12 
WHERE name = "Whiskers";

SELECT * FROM pets WHERE name = "Whiskers";
-- ✅ 6b. Update multiple pets' favorite_treats
UPDATE pets 
SET breed = "Old" 
WHERE age > 5;

-- ✅ 7. Delete data
-- DELETE FROM pets WHERE breed = "Old" OR age = 1;

-- ✅ 8. Join data 
-- ✅ 8a. One to many
-- join table to have all pet and owner data in one row
-- check if owners.id = pets.owner_id 
SELECT * 
FROM pets 
JOIN owners 
ON owners.id = pets.owner_id;

SELECT * 
FROM owners 
JOIN pets 
ON owners.id = pets.owner_id
ORDER BY pets.id ASC;

-- ✅ 8b. Many to many: create staff table 
-- ✅ 8c. Many to many: create appointments table
SELECT 
    appointments.staff,
    pets.name,
    procedures.name
FROM appointments 
JOIN pets 
    ON appointments.pet_id = pets.id 
JOIN procedures
    ON appointments.procedure_id = procedures.id;

-- show all pets, including pets that have no appointments
SELECT pets.id, pets.name, appointments.staff, procedures.name 
FROM pets 
JOIN appointments 
    ON pets.id = appointments.pet_id
JOIN procedures 
    ON appointments.procedure_id = procedures.id;

SELECT pets.id, pets.name AS pet_name, appointments.staff, procedures.name AS procedure_name
FROM pets 
LEFT OUTER JOIN appointments ON pets.id = appointments.pet_id
LEFT OUTER JOIN procedures ON appointments.procedure_id = procedures.id;

-- ✅ 9. Seed data
-- ✅ 9a. Create two staff members using ChatGPT?
-- ✅ 9b. Create six appointments using ChatGPT

-- ✅ 10. Join tables
-- ✅ 10a. Basic join
-- ✅ 10b. Basic join with specific values

-- get the 5 oldest pets

-- 1. order (sort) them
-- 2. limit them
SELECT * 
FROM pets 
ORDER BY pets.age DESC 
LIMIT 5;