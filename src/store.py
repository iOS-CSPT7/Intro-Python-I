"""
python3 store.py
The dugout
    1. running 
    2. baseball
    3. basketball
    4. exit
selec the number of a department.

attributes: 
- name 
- departments 

optional extra attributes:
- store hours
- store capacity 
"""
#composition: a "has-a" relationship
#Aggregation: a "has-a " relationship
#polymorphism : works on different data structures

from departments import Department
from products import Clothing, Swords 

class Store: 
    def __init__(self, name, departments = []): 
        self.name = name 
        self. departments = departments 

        # for dep in departments:
        #     deparment = Department(dep)
        #     self.departments.append(deparment)

    def __str__(self):
        output = ""
        output += self.name + "\n"

        for index, department in enumerate(self.departments):
            output += str(index + 1) + ". " + str(department.name) + "\n"

        output += str(len(self.departments) + 1) + ". Exit"
        return output 
        # return f'Store name is {self.name}'
        
    # def __repr__(self): 
    #     return f'Store name is {self.name}'   #can be used for debugging 

# store = Store("Empty store")

running_products = [Clothing("shorts", 45, "S", "Black"), Clothing("sweat band", 12, "L", "red")]
fencing_products = [Swords("eppe", 75, 10), Swords("Saber", 75, 5)]
# store = Store("The Dugout", [Department("Running", running_products), Department("Baseball"), Department("Basketball"), Department("Fencing"), fencing_products])
dugout_departments = [Department("Running", running_products),
                      Department("Baseball"),
                      Department("Basketball"),
                      Department("Fencing", fencing_products)]
store = Store("The Dugout", dugout_departments)

print(store)

selection = 0
while selection != len(store.departments) + 1:
    selection = input("Select the number of a department.")
    try:
        selection = int(selection)
        if selection >= 1 and selection < len(store.departments) + 1:
            print(f"the user selected: {selection}")
            print(store.departments[selection -1])
        elif selection == len(store.departments) + 1:
            print("Thank you for shopping with us today!")
        else:
            print("Choose from the given choices")
    except ValueError:
        print("Choose a number, not an empty string or a letter")
