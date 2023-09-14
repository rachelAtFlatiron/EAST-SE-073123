#!/usr/bin/env python3
class Pet:
    #✅ 1. create relationship: pet belongs to an owner
    #✅ 2. use chatGPT to create owners and pets in debug.py
    #✅ 2a. create __repr__ function to more easily read output
    def __init__(self, name, age, breed, owner):
        self.name = name
        self.age = age
        self.breed = breed
        self.owner = owner 

    #✅ 5. create relationship: pet has many appointments

    #✅ 6. create relationship: pet has many procedures (but make it unique)
