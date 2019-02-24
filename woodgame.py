x = input("Choose Left or Right to get out of wood: ")
count = 0
while count <= 1:
    if x == "Right":
        x = input("Choose again Left or Right to get out of the wood: ")
        count+=1
        if count > 1:
            print("You lose")
    elif x == "Left":
        print("You got out of the wood")
        break
        
    
