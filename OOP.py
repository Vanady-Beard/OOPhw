# Objective: The aim of this assignment is to apply the concepts of 
# Object-Oriented Programming in Python to build a simulated 
# City Infrastructure Management System. 
# This system will incorporate classes, objects, methods, and 
# data structures to manage different aspects of a city, such as 
# buildings, traffic, and events.

# Task 1: Vehicle Registration System

# Problem Statement: Create a Python class Vehicle with attributes 
# registration_number, type, and owner. Implement a method update_owner to 
# change the vehicle's owner. Then, create a few instances of Vehicle and 
# demonstrate changing the owner.

# Code Example: Provide a basic structure for the Vehicle class without methods.
#     class Vehicle:
#         def __init__(self, reg_num, type, owner):
#             self.registration_number = reg_num
#             self.type = type
#             self.owner = owner
# Expected Outcome: Completion of the Vehicle class with the update_owner method and 
# a demonstration script showing the creation of Vehicle objects and updating their owners.



class Vehicle:
        
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
        
    def update_owner(self, new_owner):
        print(f"{self.owner} is the old owner of the {self.type}. The new owner is {new_owner}")
      
car = Vehicle ("46896954", "Bentley", "Keisha") 
car1 = Vehicle ("87649032", "Nissan", "Sam")
print(car.registration_number)
car.update_owner("Salay")
car1.update_owner("Derrick")


 # Task 2: Event Management System Enhancement

# Problem Statement: Use the existing Event class by adding an attribute to 
# keep track of the number of participants. Implement a method add_participant that 
# increases the count and a method get_participant_count to retrieve the current count.
# Code Example: Basic Event class without participant tracking.
#     class Event:
#         def __init__(self, name, date):
#             self.name = name
#             self.date = date


class Event:
   
    def __init__(self, name, date, participants):
        self.name = name
        self.date = date
        self.num_participants = participants
   

    def add_participant(self,count):
        self.num_participants += count
    
    
    def  get_participant_count(self):
         print(f"The event we having on {self.date} is {self.name} and there are {self.num_participants} people comming to the event.")
        



event = Event("Lamar", "11/25/2024", 2)
# event.get_participant_count()
event.add_participant(2)
event.add_participant(3)
event.get_participant_count()

