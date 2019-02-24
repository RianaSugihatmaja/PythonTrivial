x = input("To get out of the wood, would you go Left or Right? ")
count = 0

while count <=2:
    if x == "Right":
        count+=1
        x = input("Which one again? ")
        if count > 3:
            print("You Lose")
    elif x == "Left":
        print("You Got Out of The Wood")
        break
else:
    if x == "Left":
        print("You Got Out of The Wood")
    else:
        print("You Lose")        
    
