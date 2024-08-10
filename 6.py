
# List[] in python :-

"""list = [1, 1.2, "krishna", True, 1, 2, 2]
print(list)
print(type(list))
list[1] = 2.6  # we can change indwx value in python 
print(list)"""

# list slicing
"""print(list[1 : 4])"""

# functions in list :-
"""list2 = [4, 12, 3 , 1, 6, 5]

# append function ;-
list2.append(7)  #It added the item to the end of the list 
# print(list2)

# sort function :-
list2.sort()  # it sort the list item in assending way
print(list2)

# sort reverse
list2.sort(reverse=True)
print(list2)

# reverse function :-
list2.reverse()
print(list2)

# insert function :-
list2.insert(12, 2)   # we can inser any value at any index
print(list2)          #note :- if we assign value at index that not present in list so it store the value at the last index of the list
print(list2.index(2))

#copy function:-
list2.copy()  # it copies the list
print(list2)

#pop function :-
list2.pop()  # it deletes last index's value
print(list2)

#remove function :-
list2.remove(3)   # it deletes any value we give in parenthisis 
print(list2)"""


##########################---------------------------------------###############################

# Tuples() in python:-
# example ::-    Note : tuple are immutable mean we can access values of tuples but we can not change it or assign it. 
"""tup = (1, 2, 3, 4, 5, 6, 4, 4)
print(tup, type(tup))

tup1 = ("krishna", 1, 1.2)  # so it can also cantain different data type values like list
print(tup1)

print(tup1[2]) # it print's the value that have index 2

# slicing in tuples :=
print(tup[0:3])

# Methods in tuples 

# index method 

print(tup.index(6)) # it show the index no. of give value

#count method
print(tup.count(4)) # it counts that the how many time the same value occure """

######################<<<<<<<<<<<---------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>################
# practice question ;-
"""wap to ask user to enter their 3 favroite movies and store them in list"""

# movies = []
# movies.append(input("enter first faviorite movies name:- "))
# movies.append(input("enter second faviorite movies name:- "))
# movies.append(input("enter third faviorite movies name:- "))
# print(movies)

"""WAP to check if list contain pellidrom of element, Hint use copy() method"""

# list1 = [1, 2, 3, 2, 1,]
# copy_list = list1.copy()
# copy_list.reverse()

# if(copy_list == list1):
#     print("yes, they have palindrome")
# else:
#     print("no, they not have palindrome")

"""WAP to count the number of studente with the "A" grade in the following tuple
         ["C", "D", "A", "A", "B", "B", "A"]"""
         
# tupx = ("C", "D", "A", "A", "B", "B", "A")
# print("the no. of student with grade A is:- ", tupx.count("A"))



""" Store the above values in a list & sort them from "A" to "D". """
# tupx = ("C", "D", "A", "A", "B", "B", "A")
# listx = list(tupx)
# listx.sort()
# print(listx)