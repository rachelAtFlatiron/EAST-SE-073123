#✅ 5. Import the pet and cat class to use in debug.py
#✅ 6. See pet.py
from lib.pet import Pet
#✅ 7. Create a subclass of Pet called Cat
class Cat(Pet):
    #✅ 7a. Import Pet from lib.pet

    #✅ 7b. Create an __init__ method that has all parameters of Pet including an additional parameter: indoor

    #class Pet does not have indoor attribute, indoor is meant for Cat only
    def __init__(self, name, age, breed, indoor):
        # self.name = name 
        # self.age = age 
        # self.breed = breed
        #✅ 7c. Use super to pass Pet parameters to super class
        #super().__init__ will invoke parent class' init method
        super().__init__(name, age, breed)
        self.indoor = indoor

    

    #✅ 7d. Update the instance in debug.py to rose = Cat('rose', 11, 'domestic longhair', 'sweet', 'rose.jpg', True)


    #✅ 9. Create a method unique to the Cat subclass called talk which returns the string "Meowwwwwww"
    def say_meow(self):
        print("Meow")

    #✅ 10. Create a method called print_pet_details, to match the print_pet_details in Pet    
    def print_pet_details(self):
        super().print_pet_details()
        print(f'indoor: {self.indoor}')
    #✅ 10a. Print the indoor attribute