# Sequence Types

# JS -> arrays, Python -> lists
# JS -> objects, Python -> dictionaries 

# Creating Lists
#✅ 1. Create a list of 10 pet names
# Mutable: can change values
pet_names = ["Momo", "Ejay", "Ari", "Marceline", "Abby", "Ellie", "Sarah", "Mollie", "Polar"]
banana = ['b', 'a', 'n', 'a', 'n', 'a']
#------------------------ Reading Information from Lists
#✅ 2. Return the first pet name 
#print(pet_names[3]) #Marceline

#✅ 3. Return the last value, we can work backwards through lists
#print(pet_names[-1]) #polar
#print(pet_names[-2]) #mollie

#✅ 4. Return all pet names beginning from the 3rd index
#print(pet_names[3:5]) #exclusive of the 5th index
#print(pet_names[:5]) #blank on left assumes start
#print(pet_names[5:]) #blank on right assumes end

#✅ 5. Return all pet names before the 3rd index
#print(pet_names[0:3])
#print(pet_names[:3])
#print(pet_names[:]) ##prints everything

#✅ 6.  Return all pet names beginning from the 3rd index and up to (exclusive of/not including) the 7th
#print(pet_names[3:7])

#✅ 7. Find the index of a given element
#print(pet_names.index('Abby'))

#✅ 8. Reverse the original list
#print("reverse", pet_names[ : :-1]) #not destructive, technically takes a slice (from beginning to end)
#print(pet_names.reverse()) #🛑 destructive, directly mutates pet_names, returns None
#print('after index reverse', pet_names)

#✅ 9. Return the frequency of a given element 
#print(banana.count('a'))

#---------------------------------- Updating Lists: get index, set equal to whatever
#✅ 10. Change the first element to all uppercase
pet_names[0] = pet_names[0].upper()
#find the index
abby_index = pet_names.index('Abby')
#use the found index to update
pet_names[abby_index] = pet_names[abby_index].upper()

#---------------------------------- Adding items to list
#✅ 11. Append a new name to the list
pet_names.append("Blu") #append to end of list, directly mutates list, returns None


#✅ 12. Add a new name at a specific index
#pet_names.insert(1, "Coco")
pet_names.insert(-1, "Coco") #second to last index, use append for the end
#print(pet_names)

#✅ 13. Add two lists together 
added_list = [1, 2, 3] + [4, 5, 6]
#print(added_list)

#---------------------------------- Removing 
#✅ 14. Remove the final element from the list
pet_names.pop() #directly mutates list, returns element that was popped

#✅ 15. Remove element by specific index
pet_names.pop(3)

#✅ 16. Remove a specific element 
pet_names.append('Sarah')
pet_names.remove('Sarah') #first encountered Sarah is removed

#✅ 17. Remove all pet names from the list
pet_names.clear()

#---------------------------------- Tuple 
#🛑 immutable - cannot be changed 
#✅ 18. Create a Tuple of pet 10 ages 
pet_ages = (3, 2, 6, 1, 6, 7, 2, 5)
#✅ 19. Print the first pet age
pet_ages[0]
#---------------------------------- Testing Changeability 
#✅ 20. Attempt to remove an element with .pop (should error)
#pet_ages.pop()

#✅ 21. Attempt to change the first element (should error)
#pet_ages[0] = "sldkfj"

#---------------------------------- Tuple Methods
#✅ 21. Return the frequency of a given element
pet_ages.count(6)

#✅ 22. Return the index of first matching element 
test = pet_ages.index(2)

#✅ 23. Create a range 
#start value (default is 0), stop value, step (default 1)
range_1 = range(10, 0, -1)
range_2 = range(2, 5, 1)
# for i in range_1: 
#     print(i)

#---------------------------------- Demo Sets
#✅ 24. Create a set of 3 pet foods

# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 25.  Create a dictionary of pet information with the keys name, age and breed
momo = {'name': 'momo', 
        'weight': 'fat', 
        'hobby': 'waiting for food', 
        'cuddliness': 2,
         'age': 3 } 

#✅ 26.  Use dict to create a dictionary of pet information with the keys name, age and breed
momo_dict = dict(name='momo', weight='fat', hobby='waiting', cuddliness=2, age=3)

#---------------------------------- Reading
#✅ 27. Print the pet attribute of name using bracket notation
momo['cuddliness'] #🛑 throws error if key does not exist and breaks code

#✅ 28. Print the pet attribute of age using .get
momo.get('sdlkj') #returns none

#---------------------------------- Updating 
#✅ 29. Update the pets age to 12
momo['age'] = 4 #if key exists, updates key/value pair
momo['goals'] = 'None' #if key does not exist, adds new key/value pair

#---------------------------------- Deleting
#✅ 30. Delete a pets age using the del keyword 
del momo['goals'] #won't return anything

#✅ 31. Delete the pets age using the .pop, returns removed value
momo.pop('age') #will return value

#✅ 32. Delete the last item in the pet dictionary using popitem()
momo.popitem()

#---------------------------------- Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]

#✅ 33. loop through a range of 10 and print every number within the range
for i in range(1, 10):
    # print(i)
    pass
# with a while loop 
i = 1 
while(i < 10):
    #print(i)
    i += 1

#✅ 34. loop through a range between 50 and 60 that iterates by 2 and print every number
for i in range(50, 60, 2):
    #print(i)
    pass

#✅ 35. Loop through the pet_info list and print every dictionary 
for pet in pet_info: 
    #print(pet.get('breed'))
    pass

#✅ 36. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument
def print_info(lst=pet_info):
    for pet in pet_info:
        #print(pet)
        pass
# print_info() #relies on default value
# print_info(pet_info) 

#✅ 37. Create a function that takes a list as an argument.(simple example) 
def counter(info=pet_info):
    # The function should define a counter and set it to 0
    counter = 0
    # Create a while loop 
    while(counter < len(info)): #counter <= len(info) - 1
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
        counter += 1
    # return the counter 
    return counter


#✅ 38. Create a function that updates the age of a given pet using the name
'''###
cur_index = 1
info[cur_index]  = {'name': 'spot',...}
info[cur_index].get('name') = spot
###'''
def update_age(info, name, age):
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        cur_index = 0 
        #case 1: we find an item with a matching name 
        #case 2: we have reached the end of the list
        while(cur_index < len(info) and info[cur_index].get('name') != name):
            cur_index += 1
        # If the dict containing a matching name is found update the items age with the new age 
        if(cur_index >= len(info)):
            print("error")
        else:
            info[cur_index]['age'] = age 
update_age(pet_info, 'Meow Meow Beans', 0)
#print(pet_info)

#✅ 39. Use list comprehension to return a list containing every pet name in uppercase
# .map like
pet_names_upper = [pet.get('name').upper() for pet in pet_info]
# pet_info.map(pet => pet.get('name').upper())
pets = [cur_pet.get('name') for cur_pet in pet_info]

#✅ 40. Use list comprehension to find a pet named spot
# .filter like 
find_pet = [pet for pet in pet_info if pet.get('name') == 'spot']

#✅ 41. Use list comprehension to find all of the pets under 3 years old
age_pet = [pet for pet in pet_info if pet.get('age') < 25]
print(age_pet)
# pet_info.filter(pet => pet.get('age') < 25)

#✅ 43. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
