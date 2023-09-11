# Sequence Types

# Creating Lists
#✅ 1. Create a list of 10 pet names

#------------------------ Reading Information from Lists
#✅ 2. Return the first pet name 

#✅ 3. Return the last value

#✅ 4. Return all pet names beginning from the 3rd index

#✅ 5. Return all pet names before the 3rd index

#✅ 6.  Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th

#✅ 7. Find the index of a given element

#✅ 8. Reverse the original list

#✅ 9. Return the frequency of a given element 

#---------------------------------- Updating Lists
#✅ 10. Change the first element to all uppercase

#---------------------------------- Adding items to list
#✅ 11. Append a new name to the list

#✅ 12. Add a new name at a specific index

#✅ 13. Add two lists together 

#---------------------------------- Removing 
#✅ 14. Remove the final element from the list

#✅ 15. Remove element by specific index

#✅ 16. Remove a specific element 

#✅ 17. Remove all pet names from the list

#---------------------------------- Tuple 
#✅ 18. Create a Tuple of pet 10 ages 

#✅ 19. Print the first pet age

#---------------------------------- Testing Changeability 
#✅ 20. Attempt to remove an element with .pop (should error)

#✅ 21. Attempt to change the first element (should error)

#---------------------------------- Tuple Methods
#✅ 21. Return the frequency of a given element

#✅ 22. Return the index of first matching element 

#✅ 23. Create a range 

#---------------------------------- Demo Sets (stretch goal)
#✅ 24. Create a set of 3 pet foods

# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 25.  Create a dictionary of pet information with the keys name, age and breed

#✅ 26.  Use dict to create a dictionary of pet information with the keys name, age and breed

#---------------------------------- Reading
#✅ 27. Print the pet attribute of name using bracket notation

#✅ 28. Print the pet attribute of age using .get

#---------------------------------- Updating 
#✅ 29. Update the pets age to 12

#✅ 30. Update the other pets age to 26

#---------------------------------- Deleting
#✅ 30. Delete a pets age using the del keyword 

#✅ 31. Delete the other pets age using the .pop, returns removed value

#✅ 32. Delete the last item in the pet dictionary using popitem()

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

#✅ 34. loop through a range between 50 and 60 that iterates by 2 and print every number

#✅ 35. Loop through the pet_info list and print every dictionary  

#✅ 36. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument

#✅ 37. Create a function that takes a list as an argument.(simple example) 
    # The function should define a counter and set it to 0
    # Create a while loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # return the counter 

#✅ 38. Create a function that updates the age of a given pet
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        # Create a while loop. 
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age 
        # else return 'pet not found'

#✅ 39. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase

#✅ 40. Use list comprehension to find a pet named spot

#✅ 41. Use list comprehension to find all of the pets under 3 years old

#✅ 43. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
