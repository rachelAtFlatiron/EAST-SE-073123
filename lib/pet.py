#!/usr/bin/env python3
import ipdb
#✅ 1. Create a Pet class
class Pet:
    #✅ 2. Instantiate a few pet instances in ipdb 
    #✅ 2a. Compare the pet instances to demonstrate they are not the same object
    #🛑 there is a default init if you choose not to overwrite it with your own init
    #✅ 3. Demonstrate __init__ 
    def __init__(self, name, age, breed, owner="No Owner"):
    #✅ 3a. Add parameters for attributes (NO OWNER YET, SEE 3D)
        #🛑 self refers to whatever pet is currently being created by the init method  
        self.name = name 
        self.age = age 
        self.breed = breed 
        self.owner = owner 

        #✅ 3b. use dot notation to access their attributes 
        #✅ 3c. update attributes with new values 
        #example_pet.name = "new_name" 

        #✅ 3d. add owner attribute with default value

    #✅ 4. Demonstrate INSTANCE methods
    #✅ 4a. Create a hello method that will print "Hello!"
    #🛑 when calling hello on an actual instance of pet, you won't pass in "self" -> momo.hello()
    def hello(self):
        print("hello!")

    #✅ 4b. Create a print_pet_details function that will print the pet attributes
    def print_pet_details(self):
        print(f'''
                name: {self.name} 
                age: {self.age}
                breed: {self.breed}
                owner: {self.owner}
              ''')

#✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
class Owner:
    #✅ 5d.  Add parameter to pass in name property value on instantiation
    def __init__(self, name, age, height):
        self.name = name #self.name relies on setter method instead of directly updating self._name 
        self.age = age
        # ONLY RUNS ONCE WHEN THE INSTANCE IS CREATED
        if isinstance(height, float):
            self.height = height 
        else: 
            self.height = 0.0

    #🛑 get/set instance methods good for constraints
    #✅ 5a. Create get/set instance methods for name property 
    def get_name(self):
        print("getting name...")
        return self._name #🛑 _ says this should be a private attribute
    #✅ 5b. Create constraint to make sure the name is of type string
    def set_name(self, name):
        print("setting name...")
        if isinstance(name, str):
            self._name = name   
            return self._name 
        else: 
            print("not a string")
    #✅ 5c. Compile get_name, set_name under the same property name
    name = property(get_name, set_name)

    #🛑 syntatic sugar for the above
    @property 
    def age(self):
        print("getting age...")
        return self._age 
    @age.setter  #always has to be "setter"
    def age(self, age):
        print("setting age...")
        if(isinstance(age, int)):
            self._age = age 
            return self._age 
        else: 
            print("not an integer") 

polar = Pet("polar", 2, "dog", "tano")
abby = Pet("abby", 5, "cat", "kim")
momo = Pet("momo", 2, "cat")
rachel = Owner("rachel", 28, 5)
kim = Owner("kim", 29, 5.3)
tano = Owner("tano", 30, 5.6)

ipdb.set_trace()