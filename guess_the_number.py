num=18
print("you have to guess between 1 to 100")
print("No. of guesses you have=5")
i=1
while(i<6):
    j=5-i
    gue=int(input("ENTER THE NUMBER\n"))
        
    if(gue<10):
        print("you guessed too low")
        print("you have guesses left=",j)
        i=i+1
    elif(10<gue<20 and gue!=18):
        print("you need to guess a little bit")
        print("you have guesses left=",j)
        i=i+1
    elif(20<gue<100):
        print("you guessed too high")
        print("you have guesses left=",j)
        i=i+1
    else:
        print("you guessed right")
        print("no. of guesses you took",i)
        break
    if(i>5):
        print("GAME OVER!")