# funtioms in python
"""block od statement that perform a specific task"""

# example :-
# def sum(a,b): # with argument
#     add = a + b
#     # print(add)
#     return add 

# x = print(sum(1,2))

# def print_hello():
#     print("hello there")
# print_hello()

########## practise question ##############
"""Q. find average of three numbers"""
# def avg(a,b,c):
#     print((a+b+c)/3)
    
# avg(6,26,2)

"""Q. write a function to print the length of list.(list is the parameter)"""

# marvel_heros = ["ironman", "dr.strange", "shaktiman", "blackwidow", "thor"]
# anime_heros = ["goku","naruto","luffy","asta","gojo","zoro","natsu","rimuru","tanjiro","nami"]

# def list_func(list):
#     print(len(list))
    
# list_func(marvel_heros)
# list_func(anime_heros)

"""Q. WAF to print the elements of a list in a single line.(list is the parameter)"""

# marvel_heroes = ["ironman", "dr.strange", "shaktiman", "blackwidow", "thor"]
# def list_func(list):
#     for i in list:
#         # print(i)   # it returns the value of list in next line
#         print(i, end=" ") # it return the value of list in same line, by the help of ' end = " " ' function
        
# list_func(marvel_heroes)

"""Q. WAF to find the factorial of n (n is the parameter)"""

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#       fact *= i
#     print(fact)  
      
# factorial(6)     

"""Q. WAF to convert usd into inr """

# def converter(usd):
#     print("indian rupees =",(usd * 83),"Rs")
# converter(26)

"""Q. WAf that take n number and check wheter number is even or odd"""

# n = int(input("enter the number: "))

# def check(n):
#     if(n%2 == 0):
#         print("it is even")
#     else:
#         print("it is odd")

# check(n)

#################### Recursion ####################
""" Recursion :- when a fuction calls itself repeatdly"""

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
# show(5)   

# Example of recursion :-
"""def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(6))"""


############## Practce Question of Recursion ###################

"""Q. write a recursive function to calculate the sum of first n natural numbers"""

# def sum(n):
#     if(n >= 1):
#         return n + sum(n-1)
#     else:
#         return 0
    
# print(sum(4))

"""Q. write a recursive function to print all elements in a list 
        Hint : use list & index as parameters """

anime_heroes = ["goku","naruto","luffy","asta","gojo","zoro","natsu","rimuru","tanjiro","nami"]    

def call(list, n = 0):
    if(n == len(list)):
        return
    else:
        return(list,n)

print(call(anime_heroes))