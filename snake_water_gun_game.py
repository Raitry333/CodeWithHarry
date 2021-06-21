import random
lst=["s","g","w"]
print("WELCOME TO MY GAME!!!!")
print("CHOOSE 'S' FOR SNAKE")
print("CHOOSE 'g' FOR GUN")
print("CHOOSE 'w' FOR WATER")

i=1
your_point=0
comp_point=0

while(i<11):
    inp=input("WHAT'S YOUR CHOICE?\n")
    chc=random.choice(lst)
    print(chc)
    
    if(inp=="s" and chc=="w"):
     
        print("WIN!!!!")
        your_point=your_point+1
        i=i+1
    elif(inp=="w" and chc=="s"):
        print("LOSE:(")
        comp_point=comp_point+1
        i=i+1
    elif(inp=="w" and chc=="g"):
        print("WIN!!!!")
        your_point=your_point+1
        i=i+1
        
    elif(inp=="g" and chc=="w"):
        print("LOSE:(")
        comp_point=comp_point+1
        i=i+1
    elif(inp=="g" and chc=="s"):
        print("WIN!!!!")
        your_point=your_point+1
        i=i+1
    elif(inp=="s" and chc=="g"):
        print("LOSE:(")
        comp_point=comp_point+1
        i=i+1
    elif(inp=="s" and chc=="s"):
        print("TIE")
        i=i+1
    elif(inp=="w" and chc=="w"):
        print("TIE")
        i=i+1
    elif(inp=="g" and chc=="g"):
        print("TIE")
        i=i+1
if(i>=11):
    print("GAME OVER!!!")
if(your_point>comp_point):
    print("YOU'RE THE WINNER!\n YOUR POINT IS\n",your_point)
    print("COMPUTER'S POINT IS\n",comp_point)
if(your_point<comp_point):
    print("YOU LOSE!:(\n YOUR POINT IS\n",your_point) 
    print("COMPUTER'S POINT IS\n",comp_point)
    
if(your_point==comp_point):
    print("IT'S A TIE!")
    print("YOUR POINT IS\n",your_point)
    print("COMPUTER'S POINT IS\n",comp_point)
