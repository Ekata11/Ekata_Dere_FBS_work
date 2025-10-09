#Toll calculation : 

from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,persons):
        self.persons=persons
    
class Two_Wheeler(Vehicle):
    def calculate_toll(self):
        toll =20
        if self.persons>2:
            toll+=(self.persons-2)*10
        return toll  
    
class Three_Wheeler(Vehicle):
    def calculate_toll(self):
        toll =30
        if self.persons>3:
            toll+=(self.persons-3)*30
        return toll
    
class Four_Wheeler(Vehicle):
    def calculate_toll(self):
        toll=40
        if self.persons>4:
            toll +=(self.persons-4)*40
        return toll

class Heavy_Vehicle(Vehicle):
    def calculate_toll(self):
        toll=60
        if self.persons>60:
            toll+=(self.persons-60)*100 
        return toll   

while True:
   
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    ch = int(input("Enter choice: "))
    if ch == 5:
        break

    p = int(input("Enter number of persons: "))
    if p < 1:
        print("Number of persons must be at least 1.")
        continue

    if ch == 1:
        vehicle = Two_Wheeler(p)
    elif ch == 2:
        vehicle = Three_Wheeler(p)
    elif ch == 3:
        vehicle = Four_Wheeler(p)
    elif ch == 4:
        vehicle = Heavy_Vehicle(p)
    else:
        print("Invalid choice!")
        continue

    print("Total toll to pay:", vehicle.calculate_toll())


