print("WELCOME TO THE CALCULATOR")
print("'+' -addition")
print("'-' -subtraction")
print("'*' -multiplication")
print("'/' -division")
print("'**' -power")
print("'%' -remainder")
print("enter your operator")
op=input()
print("enter first number")
first=int(input())
second=int(input("enter second number\n"))
if(op=="+" and first==56 and second==9):
    print("ans-77")
elif(op=="+"):
      print("ans-",first+second)
elif(op=="*" and first==45 and second==3):
    print("ans-555")
elif(op=="*"):
       print("ans-",first*second)
elif(op=="/" and first==56 and second==6):
    print("ans-4")
elif(op=="/"):
        print("ans-",first/second)
elif(op=="-"):
    print("ans-",first-second)
elif(op=="**"):
    print("ans-",first**second)
elif(op=="%"):
    print("ans-",first%second)
else:
    print("TRY AGAIN!")