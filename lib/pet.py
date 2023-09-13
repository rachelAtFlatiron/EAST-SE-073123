#!/usr/bin/env python3
# Class Attributes and Methods 

#✅ 5. Import the pet and cat class to use in debug.py

#✅ 6. Keep track of the total number of Pets created
class Pet:
    #✅ 6a. Create a class attribute
    total_pets = 0 

    def __init__(self, name, age, breed):
        self.name = name 
        self.age = age 
        self.breed = breed 
        #✅ 6b. Update class attribute whenever an instance is initialized
        #Pet.total_pets = Pet.total_pets + 1
        Pet.increase_pets()

    #✅ 6c. Create a class method increase_pets that will increment total_pets
    @classmethod 
    #because this is a class method, instead of self, pass in cls
    def increase_pets(cls):
        cls.total_pets += 1

    def print_pet_details(self):
        print(f'''
            name:{self.name}
            age:{self.age}
            breed:{self.breed}
        ''')
