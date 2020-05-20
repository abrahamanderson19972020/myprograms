#This a program that finds age
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



