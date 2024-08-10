import random
target = random.randint(1,100)

while True:
    userchoice = (input("Guess the Target or Quit : "))
    if(userchoice == "Quit"):
        break
    
    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success: correct guess")
        break
    elif(userchoice < target):
        print("your number is too small. take a bigger guess")
    
    elif(userchoice > target):
        print("your number is too big. Take a small guess")
        
print("----------GAME OVER---------")
    
    