"""type conersion :- it converts the datatype implicitly """

# for example :-
# val1 = 5
# val2 = 10.5
# add = val1 + val2   #it converts integer into float
# print(add)

""" type casting :- we converts the datatype explicitly by appling datatypes """

# for example :-
# a = 5
# b = "2"
# sub = a - int(b)   #we convert string into intiger
# print(sub)

# user input 
user = input("enter the value :- ")
user1 = int(input("enter the value :- "))

output = int(user) + user1
print(output)
