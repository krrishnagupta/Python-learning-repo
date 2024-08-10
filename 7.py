# dictionary in python :-
dict = {}  # it is null dict. fi want we can add key- values latre

# Example :=         Note : dictionary is mutable and can not store duplicate values
"""detail = {
    "name": "krishna",          #here, 'name' is "key" and 'krishna' is "value" of that key
    "branch": "CSEIML",
    "roll-no": 26,
    "phone": 123456
}

print(detail)
print(type(detail))
print(detail["name"]) # access one key 
print(detail["phone"])"""

# Nested dictionary :-

student = {
    "name": "krishna kumar gupta",
    "roll-no": 70679191660,
    "subject":{
        "nlp": 37,
        "aoc": 28,
        "ds": 49,
        "se": 45,
        "apt": 43
    },
    "branch": "CSE-IML"
} 
# student["roll-no"] = 26 #it overwrite the previuos value
# print(student)

# print(len(student))  # length of dictionary

# print(len(list(student.keys())))  # convert into list than find the length

#### Dictionary methods :-

"""# dict.keys() :-
print(student.keys()) # returns all keys

# dict.values():-
print(student.values()) # return all values

# dict.items() :-
print(student.items()) #return all key value pairs as tuple

# dict.get() :-
print(student.get("name")) #return keys according to values, if key is not present it returns "none"

# dict.update(new_dict) :-
student.update({"city":"khargone"}) #insert the specifiesd item to dictionary
print(student)"""

#################-----------------------#########################
"""Sets in python :-
        note : set is collection of unorederd items
               each element in the set must be immutable and unique 
               and the set is mutable""" 

# example :-
# set = {1,2,3,4, "hello","kk", 5}
set = {1, 1.2, "krishna", True, (2, 1, 3.3)} 
# print(set)
# print(type(set))

# methods in sets :-

"""#set.add(x) :-
set.add("new_word")  # add new element
print(set)

# set.remove(x) :-
set.remove("new_word")  # remove element
print(set)

#set.pop() :-
set.pop()
print(set)    # it remove a random value

#set.clear() :-
set.clear()
print(set)  # it empties the set"""

# other two important sets :-

"""# union & Intersection :-
set1 = {1, 2, 3, 4, 5, 6}
set2 = {2, 4, 6, 8, 10}

print(set1.union(set2)) # it prints all the uniqe values

print(set1.intersection(set2)) # it prints all the common value in set"""


############-------------&&&&&&&&&&&&&&&--------------################

# Practise Questions :-
"""Q1.  store following word meanning in dictanory :
        "table" : "a piece of furniture", "list of facts and figure"
        "cat" : "a small animal" """
    
# store = {}

# store.update({"table" : ["a piece of furniture", "list of facts and figure"],
#               "cat": "a small animal"})
# print(store)

"""Q2.  you are give a list of subject for a student, assume one class room is requerid for one subject. how many classs room is needed for all subjects
        subjects :- "python", "java", "javascript","python", "c++", "c", "java","python", "c++" """
    
# subjects = {"python", "java", "javascript","python", "c++", "c", "java","python", "c++"}
# print(subjects)
# classroom = len(subjects) 
# print(classroom)

""" Q3. WAP to enter the marks of three subjects from the user and store them in dictionary. 
        start with an empty dictionary and add one by one. & use subject name as key and marks as a value"""
        
# marks = {}

# phy_marks = int(input("enter physics marks : "))
# marks.update({"physics": phy_marks})

# math_marks = int(input("enter maths marks : "))
# marks.update({"maths": math_marks})

# eng_marks = int(input("enter english marks : "))
# marks.update({"english": eng_marks})  

# print(marks)

""" Q4. figure out a way to store 9 & 9.0 as a seprate value in the set
        (you can take help of built in data types)"""
        
        # way 1 :
num = {9, "0.9"}
print(num)

        # way 2 :
num1 = {
    ("int", 9),("float", 9.0)
}
print(num1)