## super method :-
"""super method is used to access methods of the parent class"""
# Example :-

"""class car:   # parent
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car is stop..")
        
        
class honda(car):   #child
    def __init__(self, name,type):
        super().__init__(type)   # super method accessing __init__() function
        self.name = name
        
car1 = honda("delax", "petrol")
print(car1.type)"""
        
## class method :-
"""A class method is bound to the class and recive the class as an implicit first argument"""
"""Note : static method can't access or modify class state & generally for utility"""

# class person:
#     name = "anonymus"
    
#     @classmethod
#     def changename(cls,name):
#         cls.name = name
        
# p1 = person()
# print(person.name)   # name remain same --- "anonymus"

# p1.changename("krishna kumar gupta") # name is changed = "krishna kumar gupta"
# print(person.name)      # name is changed = "krishna kumar gupta" 
# print(p1.name)

##Property
"""we use @property decorator on any method in the class to use method as a property """
# Example :-

# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy
#         self.che = che
#         self.math = math
        
#     @property
#     def percentage(self):
#         return str((self.phy + self.che + self.math) / 3) + "%"
    
    
# krishna = Student(90, 90, 90)   
# print(krishna.percentage)

# krishna.phy = 99
# print(krishna.percentage)


######################### polimorphism : operator overloding #####################

"""when the same operator is allowed to have a diffrent meaning according to the context"""
# Example :-
"""print(1 + 2)
print("krishna " + "gupta")
print([1, 3, 4, 5] + [2, 6, 8, 10])"""


# polimorphism example :

"""class complex:
    
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def show(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self, num):    #  __add__ is an a "Dunder" function, and there are different dunder function like : __sub__ , __mul___ , __truediv___,  __init__
        newreal = self.real + num.real
        newimg = self.img + num.img
        return complex(newreal, newimg)

num1 = complex(6, 26)
num1.show()
num2 = complex(26, 6)
num2.show()
num3 = num1 + num2
num3.show()"""

################### Practise question ########################

"""Q. Define a circle class to create a circle with radius R using the constructor.
      define a area() method of class which calculates the area of circle.
      define a perimeter() method which allow you to calculate the perimeter of a circle """
      
# #Sol :   
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return(22/7) * self.radius ** 2
        
#     def perimeter(self):
#         return 2 * (22/7) * self.radius
    
# num = Circle(26)
# print(num.area())
# print(num.perimeter())

"""Q. define a Employee class with attribute salary, role & department. This class showDetails() methods
      create an a enginner class that inherits properties from employee class and has attributes : name, age"""
# #sol:

# class Employee:
#     def __init__(self, salary, role, department):
#         self.salary = salary
#         self.role = role
#         self.department = department 
        
#     def showdetails(self):
#         print("salary : ", self.salary)
#         print("role : ", self.role)
#         print("depart. : ", self.department)
        
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("name:", self.name,"\n""age:", self.age)
#         super().__init__(1200000,"full-stack dev.", "engineering") 
        
# emp1 = Employee("60000","frontend developer","Enginnering")
# emp1.showdetails()

# emp1 = Engineer("krishna", "21")
# emp1.showdetails()

# emp2 = Engineer("sneha", "21")
# emp2.showdetails()

"""Q. Create a class called Order which stores item & its price.
       use dunder function __gt__() to convey that: 
            order1 > order2 if price of order1 > price of order2"""
## sol:

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, ord):
        return self.price > ord.price
    
order1 = Order("chips", 20)
order2 = Order("biscut", 10)
# comporder = order1 < order2
comporder = order1 > order2
print(comporder) 