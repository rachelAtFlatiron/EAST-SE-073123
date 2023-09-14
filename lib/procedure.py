# ✅ 5. Use procedure 
# ✅ 5a. Use chatGPT to create some procedures
# ✅ 5b. Update appointments.py to use procedures

from appointments import Appointment
class Procedure:
    #only one procedure instance of checkup
    #can change checkup to physical exam in this instance
    #rather than updating 10 appointments from "checkup" to "physical exam"
    def __init__(self, name, price):
        self.name = name 
        self.price = price


    #return all appointments associated with current procedure
    def appointments(self):
        return [app for app in Appointment.all if app.procedure == self]
    
    #get all associated pets through appointments()
    def pets(self):
        return list(set([app.pet.name for app in self.appointments()]))
    

    def __repr__(self):
        return f'''<Procedure {self.name} is ${self.price}>'''

