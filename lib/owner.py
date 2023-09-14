from pet import Pet
class Owner:
    def __init__(self, name, phone, email):
        self.name = name 
        self.phone = phone 
        self.email = email 

    #✅ 3. create relationship: owner has many pets
    def pets(self):
        # owner_pet_list = [] 
        # #loop through all pets
        # for pet in Pet.all:
        #     #if current pet matches current owner (self)
        #     if(pet.owner == self):
        #         #append to owner_pet_list
        #         owner_pet_list.append(pet)
        owner_pet_list = [pet for pet in Pet.all if pet.owner == self]
        return owner_pet_list

    #✅ 9a. create helper method for all appointments of owner (owner has many appointments through pets)
    def appointments(self):
        #get all appointments for each pet
        apps = []
        for pet in self.pets():
            for app in pet.appointments():
                apps.append(app)
        return apps 

    #✅ 9. create a function for the total bill of the owner
    def bill(self):
        bill = 0
        for app in self.appointments():
            bill += app.procedure.price  #price is through appointment's procedure
        return f'''{self.name} owes ${bill}'''

    
    def __repr__(self):
        return f'''<Owner {self.name}>'''
    