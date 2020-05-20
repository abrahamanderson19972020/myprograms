def age_finder():
    age= int(input("PLease enter your guess :"))
    while True:
        
        if age != 34:
            age= int(input("Try again:"))
            if age > 34:
                print("Your guess is too high")
            else:
                print("Your guess is too low")
        else:
            print("Weldone")
            break
    return age
            

print(age_finder())



""" Christmas Tree """
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for item in picture:
    for i in item:
        if i==0:
            
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print("")

""" The end of the program of Christmas tree"""

#Guessing game:
import random

while True:
    
    try:
        number=random.randint(0, 10)
        guess = int(input("Please enter your guess between 1-9 :"))
        if 0 < guess < 10: 
            if number == guess:
                print("Welldone. Your guess is right")
                break
            else:
                print(f"The aswer was {number}")
        else:
            print("Your guess should be between 0 and 9!")
    except ValueError as err:
        print(err)