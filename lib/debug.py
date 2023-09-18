#!/usr/bin/env python3

from owner import Owner, CONN, CURSOR
from pet import Pet, CONN, CURSOR

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
db_path = os.path.join(dir_path, "/resources.db")


pet1 = Pet("Fluffy", 2, "Labrador")
pet2 = Pet("Whiskers", 1, "Siamese")
pet3 = Pet("Buddy", 3, "Golden Retriever")
pet4 = Pet("Mittens", 2, "Persian")
pet5 = Pet("Rocky", 4, "Bulldog")
pet6 = Pet("Luna", 1, "Husky")
pet7 = Pet("Oliver", 5, "Maine Coon")
pet8 = Pet("Charlie", 2, "Poodle")
pet9 = Pet("Daisy", 3, "Beagle")
pet10 = Pet("Max", 4, "German Shepherd")

pet1.save()
pet2.save()
pet3.save()
pet4.save()

import ipdb; ipdb.set_trace()
