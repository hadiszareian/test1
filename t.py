class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        
    def __str__(self):
        return f"this is a {self.brand} in {self.color}"

c1 = Car("Benz", 2026, "Red")
c2 = Car("BMW", 2020, "Blue")
c3 = Car("206", 2022, "white")

class Student:
    major = "CS"
    university = "Shiraz"
    max_years = 5

s1 = Student()    
s2 = Student()  