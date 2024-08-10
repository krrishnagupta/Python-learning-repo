# String in python :- we can not change index value in string
"""string = "krishna kumar gupta"
print(string)
print(len(string)) #show rhe length of string
print(string[6]) #show index value of string """


# Slicing :-
"""str1 = "slicing is the part of the string"
print(str1[10 : 19]) # it show string from 10th index to 18th index value
print(str1[ : len(str1)])  # from starting to the length of string
print(str1[-15 : -10])  # it start from right side comes to right side"""

# functions of string :-
"""str2 = "some random string"
print(str2.capitalize()) #it capatalize the first word of the string
print(str2.endswith("ing")) # it returns true if the string ends with derived value
print(str2.replace("random","given")) # it change the value from old one to new one "str.replace("old", "value")"
print(str2.find("string")) # retrun first index of first occrence
print(str2.count("s")) # it counts the occurence of word"""


# Practice question
""" write a program to input user's first name and print it's length"""
user = input("enter your first name :- ")
print(user)
print(len(user))

"""write program to find the occurence of $ in string"""
str = "find the occurence of $, if $ is present then count function give the value of occerence of $"
print(str.count("$"))