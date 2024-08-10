from tempCodeRunnerFile import i

# while loop :-
# example :
"""i = 1
while i <= 10:
    print(i)
    i += 1"""
    
############## While loop practise question ################

"""Q. print numbers from 100 to 1 """
# num = 100
# while num >= 1:
#     print(num)
#     num = num - 1
    
"""Q. print multiplication table of number n"""
# table = int(input("enter the number: "))
# i = 1
# while i <= 10:
#     print(table, "*", i, "=", table*i)
#     i = i+1

"""Q. print the element using loop
       [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#     print(nums[i])
#     i += 1
    
"""Q. search for x in this tupkle 
    (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)"""
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# j = 0
# while j < len(tup):
#     if(x == tup[j]):
#         print("found", x , "at", j)
#     else:
#         print("not find")
#     j = j+1

################# break and continue #######################
"""break statment :-"""
# i = 1
# while i <= 10:
#     print(i)
#     if(i == 6):
#         break  # it breaks the loop
#     i +=1

"""continue statment :-"""   
# j = 0
# while j <= 10:
#     if(j % 2 == 0):
#         j += 1
#         continue # it skip the value
#     print(j)   
#     j += 1

######################################### for loop ############################################
"""Loops are used for sequential traversal. for traversing list, tuple, string etc"""
# syntax :-
"""list = [1,2,3,4,5,6]
for i in list :    # i is keyword used for accessing elements( we can take any character)
    print(i)
else:
    print("end")"""
    
### fro loop practice question

"""Q. print the element using for loop
       [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"""
       
# loop_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for i in loop_list:
#     print(i)

"""Q. search for x in this tupkle 
    (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)"""
    
# loop_tup =  (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 16
# indx = 0            # if we want to check index, we must have declare it first
# for el in loop_tup:
#     if(x == el):
#         print("x find at ", indx)
#     indx += 1

### Range() function :-
"""range function return a seqence of numbers, starting from 0 by default, and increments 1 by default,  and stop before a specified number """  

# syntax :- range(start, stop, step)
# for i in range(0, 20, 2):
#     print(i)
    
### Practice Question :-
"""Q. print number from 1 to 100 """
# for i in range(1, 101):
#     print(i)

"""Q. print number from 100 to 1 """
# for i in range(100, 0, -1):
#     print(i)
    
"""Q. print the multiplication table of n number"""
# x = int(input("enter the number for table: "))
# for i in range(1, 11, 1):
#     print(x, "*", i, "=", x*i)

###### Pass keyword :-
"""pass is null statment that does nothing, it uses a placeholder for a future code"""
# example :-
# for i in range(10):
#     pass
# print("some useful code")
 
 

############################### Practice question ###################################
"""WAP to find the sum of first n numbers"""
# num = int(input("enter the number : "))
# sum = 0
# i = 1
# while i <= num:
#     sum = sum+i
#     i += 1
# print("total sum is: ", sum)

"""WAP to find the factorial of first n numbers"""
num = int(input("enter the number : "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(fact)