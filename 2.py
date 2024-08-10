# conditional statments :-
"""if-elif-else"""

# example of "if-else" trafic light code:

"""light = input("enter the color: ")
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("slow down")
else:
    print("traffic light is not working")"""

# single line conditional statments or "Ternary opreator" :-
""" <var> = <val1> if <condition> else <val2> """
   # For example :-
   
"""x = int(input("enter the value: "))
num = 5 if (x == 5) else "value is not match"
print(num)"""

# onother way:-
# <stm1> if <condition> else <stm2> 
# for example :-

"""sweet = input("enter food name:- ")
print("my favorit") if sweet == "rasmalai" or sweet == "rasgulla" or sweet == "kaju katli" else print("not my favorit")"""

# Cleaver if Ternary operator :-
# <var> = ("fals_val", "true_val") [<condition>]
# for example:-

"""age = int(input("enter your age :- "))
for_vote = ("not eligible", "yes eligible") [age >= 18]
print(for_vote)"""

# second example :-
"""salary = float(input("enter your salary :- "))
tax = salary*(0.1, 0.2) [salary >= 50000]
print(tax)"""


# Practise question :-
"""WAP to check the number entered by the user is even or odd"""

# userinpt = int(input("enter the value :- "))
# if(userinpt / 2):
#     print("the value is even")
# else:
#     print("the value is odd")
    
"""WAP to find the greatest of 3 numbers entered by user"""

# val1 = int(input("enter the first value :- "))
# val2 = int(input("enter the second value:- "))
# val3 = int(input("enter the third value :- "))

# if(val1 > val2 and val1 > val3):
#     print("value one is greater than other two")
# elif(val2 > val3 and val2 > val1):
#     print("value 2 is greater than the other two")
# elif(val3 > val2 and val3 > val2):
#     print("value 3 is greater than the other two")
# elif(val1 == val2 == val3):
#     print("they all are equal")

"""WAP to check the number is multiple of 7 or not"""

num = int(input("enter the number :- "))
if(num % 7 == 0):
    print("yes, it is multiple of seven")
else:
    print("no, it is not a multiple of seven")