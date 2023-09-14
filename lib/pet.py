#!/usr/bin/env python3
from appointments import Appointment
class Pet:
    all = []
    #✅ 1. create relationship: pet belongs to an owner
    #✅ 2. use chatGPT to create owners and pets in debug.py
    #✅ 2a. create __repr__ function to more easily read output
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner 
        Pet.all.append(self)

    #✅ 5. create relationship: pet has many appointments
    def appointments(self):
        #a. loop through all the appointments
        return [app for app in Appointment.all if app.pet == self]
        #b. if appointment matches pet, include the appointment

    #✅ 6. create relationship: pet has many procedures (but make it unique)
    def procedures(self):
        #look through all the appointments()
        #return the name of the procedure
        #use set() to turn list into set such that there are no duplicates
        #turn that set back into a list
        return list(set([app.procedure.name for app in self.appointments()]))
    
    def print_pet_details(self):
        print(f'''
            name: {self.name}
            age: {self.age}
            breed: {self.breed}
               ''')

    #✅ 10. add all bills for current pet
    def bills(self):
        bills = 0 
        for app in self.appointments():
            bills += app.procedure.price 
        return f'''{self.name} racked up ${bills}'''

    def __repr__(self):
        return f'''<Pet {self.name} the {self.breed} belongs to {self.owner.name}>'''
