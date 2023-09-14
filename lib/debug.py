#!/usr/bin/env python3
#✅ import owner, pet, and appointments
import ipdb;

from owner import Owner
from pet import Pet 
from appointments import Appointment
from procedure import Procedure


owner1 = Owner("John Doe", "123-456-7890", "john@example.com")
owner2 = Owner("Alice Smith", "987-654-3210", "alice@example.com")
owner3 = Owner("Bob Johnson", "555-123-4567", "bob@example.com")
owner4 = Owner("Eva Green", "444-789-1234", "eva@example.com")
owner5 = Owner("David Lee", "777-222-3333", "david@example.com")

# Create 10 instances of the Pet class with hardcoded data
pet1 = Pet("Fluffy", 2, "Labrador", owner1)
pet2 = Pet("Whiskers", 1, "Siamese", owner2)
pet3 = Pet("Buddy", 3, "Golden Retriever", owner3)
pet4 = Pet("Mittens", 2, "Persian", owner3)
pet5 = Pet("Rocky", 4, "Bulldog", owner5)
pet6 = Pet("Luna", 1, "Husky", owner5)
pet7 = Pet("Oliver", 5, "Maine Coon", owner2)
pet8 = Pet("Charlie", 2, "Poodle", owner3)
pet9 = Pet("Daisy", 3, "Beagle", owner4)
pet10 = Pet("Max", 4, "German Shepherd", owner5)

proc1 = Procedure("Checkup", 50)
proc2 = Procedure("Vaccination", 90)
proc3 = Procedure("Surgery", 1000)
proc4 = Procedure("Dental Cleaning", 30)

appointment1 = Appointment("Dr. Smith", pet2, proc1)
appointment2 = Appointment("Dr. Johnson", pet7, proc2)
appointment3 = Appointment("Dr. Brown", pet3, proc3)
appointment4 = Appointment("Dr. Smith", pet8, proc1)
appointment5 = Appointment("Dr. Johnson", pet5, proc2)
appointment6 = Appointment("Dr. Brown", pet2, proc3)
appointment7 = Appointment("Dr. Smith", pet9, proc1)
appointment8 = Appointment("Dr. Johnson", pet4, proc2)
appointment9 = Appointment("Dr. Brown", pet6, proc3)
appointment10 = Appointment("Dr. Smith", pet10, proc1)
appointment11 = Appointment("Dr. Johnson", pet2, proc2)
appointment12 = Appointment("Dr. Brown", pet3, proc3)
appointment13 = Appointment("Dr. Smith", pet5, proc1)
appointment14 = Appointment("Dr. Johnson", pet8, proc4)
appointment15 = Appointment("Dr. Brown", pet7, proc3)
appointment16 = Appointment("Dr. Smith", pet2, proc1)
appointment17 = Appointment("Dr. Johnson", pet6, proc4)
appointment18 = Appointment("Dr. Brown", pet4, proc3)
appointment19 = Appointment("Dr. Smith", pet3, proc1)
appointment20 = Appointment("Dr. Johnson", pet10, proc4)

ipdb.set_trace()