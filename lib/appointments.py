class Appointment:
    all = []
    #✅ 4. create relationship: appointment belongs to a pet
    #✅ 4a. use chatGPT to create instances

    def __init__(self, staff, pet, procedure):
        self.staff = staff 
        self.pet = pet 
        self.procedure = procedure
        Appointment.all.append(self)

    #✅ 7. Create a function that prints details for the appointment 
    def print_appointment(self):
        #can still access methods for outside classes 
        print (f'''
            {self.pet.print_pet_details()} 
            has a {self.procedure.name} appointment with {self.staff}
        ''')
        
    #✅ 8. Create a class method for all unique clients of the clinic
    @classmethod
    def clients(self):
        clients = []
        #appointment.all -> pet -> owner
        for app in Appointment.all:
            clients.append(app.pet.owner.name)
        return list(set(clients))

    def __repr__(self):
        return f'''<Appointment for {self.procedure.name} for {self.pet.name}>'''