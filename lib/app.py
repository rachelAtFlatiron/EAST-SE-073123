# pipenv install: install dependencies for this project
# pipenv shell: activate environment containing all dependency packages

import ipdb 

before_ipdb = "before_ipdb"

# set breakpoint, create pause in execution of code to experiment with code that has run so far
#ipdb.set_trace()

after_ipdb = "after_ipdb"

# python -> don't need let, const
# python -> always have to assign value to newly created variable
pet_mood = "Hungry!"
pet_name = "Rose"

#✅ 1. Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."
if pet_mood == "Hungry!": # triple equal does not exist in python
    # in python, string interpolation: f'{string_to_be_interpolated}'
    print(f'{pet_name} needs to be fed') 
elif pet_mood == "Rowdy!": 
    print(f'{pet_name} needs a walk') 
else: 
    print(f'{pet_name} is all good')

#✅ 2. Create a ternary operator using "pet_mood" as a condition:
# JS: condition ? true : false
# "true" if condition else "false" 
print(f'{pet_name} needs to be fed') if pet_mood == "Hungry!" else print(f'{pet_name} is all good')

#✅ 3. Create a function (say_hello) that returns the string "Hello, world!"
# JS -> function, python -> def 
def say_hello(name):
    return f"Hello, {name}!"
print(say_hello("Rachel"))
#HAVE TO PASS IN VALUE FOR ALL PARAMETERS
#print(say_hello()) #TypeError: say_hello() missing 1 required positional argument: 'name'

#🛑 runs because we set parameter to have a default value
def default_hello(name="Foster's"):
    print (f"Hello, {name}!")
default_hello() 

#✅ 4. Create a function (pet_greeting) that will return a string with interpolated pet's name

def pet_greeting(name):
    global inner_pet_name #similar to javascript, forcing it to be global
    inner_pet_name = "Tulip"
    print(f"Hello pet {pet_name}") #pet_name is from global scope (top of file)
pet_greeting('momo')
inner_pet_name #accessible outside of pet_greeting since we defined it with 'global' keyword


#✅ 5. Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!":
        print(f'{pet_name} needs to be fed') 
    elif pet_mood == "Rowdy!": 
        print(f'{pet_name} needs a walk') 
    else: 
        print(f'{pet_name} is all good')
pet_status(pet_mood="Rowdy!", pet_name="moona") 

#✅ 6. Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"
def pet_birthday(age):
    # try: # make sure user is passing in integer
    #     new_age = age + 1
    #     print(f'Happy Bday, you are now {new_age}')
    # except TypeError: 
    #     print(f'age must be of type int') #test this by passing in string
    # except NameError: 
    #     print(f'all variables must exist') #test this by deleting new_age
    # new_age = age + 1 
    # print(f'Happy Bday, you are now {new_age}')   
    if isinstance(age, int):  #type(age) == int
        new_age = age + 1
        print(f'Happy Bday, you are now {new_age}')
    else: 
        print('Error')
    
pet_birthday('sdf')
pet_birthday(3)


