# OOPs in python
"""to map the real world scenarios, started using obejects in code
    this is called object oriented programming"""
    
# Class & Object in python
""" class is an a blueprint of an a object"""
# Example :-
"""
# creating class 
class student:
    name = "krishna"
    
# creating object (instance)
s1 = student()
print(s1.name)

"""

##########    _ _init_ _ function    ###########

# Constructor
"""All classes have a function called __init__(), which is always executed when the class is being initialted"""


"""
class Students: 
    # default constructor
    def __init__ (self):  
        pass
    
    # parameterized constructor
    def __init__(self, name, marks): # the "self" parameter is a refrence to the current instance of the class, and is used to access variables that belongs to the class
        self.name = name
        self.marks = marks
        print("adding new student in database..")
        
s1 = Students("krishna",100)
print(s1.name)

s2 = Students("sneha",100)
print(s2.name)

"""


############# Practise Question #############
"""create stuent class that takes name & marks of 3 subjects as arguments in constructor, then create a method to print the average."""

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("your avaerage score is: ", sum/3)      
        
# s1 = Student("krishna gupta",[99,100,98])
# s1.avg()


######### Static method ##########
# class student:
#     @staticmethod #decorator
#     def college():
#         print("ips_academhy")
        
"""
    Decorator allow us to wrap another function in order to extend 
    the behaviour of the wraped function, without permanently modifying it
"""

########## Important ############

"""
Abstraction :- hiding the implementation details of a class and only showing the essential features to the user.
"""

"""
Encapsulation :- Wrapping data and functions into a single unit (object).
"""

######### Practise Question ############
"""Q. create account class with 2 attributes- balance and Account no.
        create methods for debit, credit & printing the balance."""
        
        
# class Account:
#     def __init__(self, balance, account_no):
#         self.balance = balance
#         self.account_no = account_no
        
#         # debit metod
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.",amount, " is debited.")
#         print("Total balance is: ",self.org_balance())

#         # credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.",amount, " is credited.") 
#         print("Total balance is: ",self.org_balance())  
        
#         # balance method
#     def org_balance(self):
#         return self.balance     
    
    
# acc1 = Account(100000, 8080211026)
# acc1.debit(1000)
# acc1.credit(500)

# del keyword :- used to delete object
# class me:
#     def __init__(self, name, no):
#         self.name = name
#         self.no = no 
        
# iam = me("krishna",26)
# print(iam.name)

# del iam.name
# print(iam.name)    # it will print error because the 

########### Private (like) methods and attributes
"""conceptual implementation in python
private method and attribute are meant to be used with in the class and not accessible from tha outside""" 
# Example:-

# class account:
#     def __init__(self,name,pwd):
#         self.name = name
#         self.__pwd = pwd   # private attribute
        
#     def private(self):
#         print(self.__pwd)
        
# a1 = account("krishna","acvd")

# # print(a1.name)
# print(a1.private())

#################### Inheritance ####################
"""when one class(child) derives the property of another class(parent/base) is called inheritance """
"""Types of inheritance :-
                single inheritance
                multi-level inheritance
                multiple inheritance"""
                
# example of single inheritance :-

# class car:   # parent
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")
        
#     @staticmethod
#     def stop():
#         print("car is stop..")
        
# class honda(car):   #child
#     def __init__(self, name):
#         self.name = name
        
# car1 = honda("xyz")   #calling child 
# print(car1.name, car1.start()) 


# example of multi-level inheritance :-

"""class car:   # parent
    color = "black"
    @staticmethod
    def start():
        print("car started..")
        
    @staticmethod
    def stop():
        print("car is stop..")
        
class honda(car):   #child
    def __init__(self, name):
        self.name = name
        
class tata(honda):
    def __init__(self, type):
        self.type = type
        
car1 = honda("xyz")   #calling child 
print(car1.name) 

car2 = tata("petrol")
print(car2.color)"""

# example of multiple inheritance :-
class A:      # parent class
    varA = "welcome to class A"
        
class B:      # parent class
    varB = "welcome to class B"
        
class C(A,B):  # child class
    varC = "welcome to class c"

print(A.varA)
print(B.varB)

print(C.varA, "and", C.varB)    # it inherit all the property of class A & B


