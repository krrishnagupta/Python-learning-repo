# File Input/Output in python
"""python can be used to perform operations on file.(read & write data)"""
#syntax :-
"""f = open("file-path", "mode") mode = r, w, a, x, b etc"""

# read operation
"""file = open("10_data.txt", "r")

# data = file.read() # it read all the data at same time 
# print(data)

data1 = file.readline() # it reads data line by line
data2 = file.readline() 
print(data1)
print(data2)
file.close()"""

#write operation :-
"""
file = open("10_data.txt", "wt") # 'w' stands for write and 't' stands for text file (defalut)

data = file.write("write operation first remove all previous data and print new data 2+6 = 26")

file.close()
"""

#append operation :-
"""
file = open("10_data.txt", "at") # 'w' stands for write and 't' stands for text file (defalut)

data = file.write("\n it's append operation it append the writen data next to previous data")

file.close()
"""

# with syntax 
"""with open("file_path", "mode") as  f:
    data = f.mode()"""
    
# example :-
"""with open("6.py", "r") as f:
        data = f.read()
        print(data)"""
        

#####################################   Deleting a File  ###########################################

"""
using os module
MOdule is (like a code library) is a file written by another programmer that generally has a function we can use

""" 

# import os

# os.remove("10_data.txt")

###################################  Practice question  ###############################################

"""Q. create a new fle "practise.txt". Add the following data in it

    hi every one 
    we are learning file input/output
    using java
    i like programming in java"""
    
# f = open("practice.txt", "w")

# data = f.write("hi every one \n")
# data = f.write("we are learning file input/output \n")    
# data = f.write("using java \n")  
# data = f.write("i like programming in java \n") 

# f.close()   
    
"""Q. WAF that replace all the occurence of a java with python"""
# with open("practice.txt","r")as f:
#     data = f.read()
    
# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt","w") as f:
#     data = f.write(new_data)


"""Q. search if the word "learning" is exist or not in file"""
def checkword():
    word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
        if(("learning") != -1):
            print("found")
        else:
            print("not found")
            
checkword()

"""Q. WAF to find in which line of te file that the word  "learning" occurse first, print -1 if word is not found """

def checkline():
    word = "learning"
    data = True
    lineno = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(lineno)
                return
            lineno += 1
    return -1

checkline()
        
"""Q. from a file containg numbers seprated by the comma, print the count of even numbers"""
count = 0
with open("practise2.txt", "r") as f:
    data = f.read()
    
    nums =  data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count +=1
            
    print(count)