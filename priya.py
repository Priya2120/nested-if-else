num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
symbol=(input("any symbol: "))
if num1>=1 and num2>=1:
    if symbol=="+":
        print(num1+num2)
    elif symbol=="-":
        print(num1-num2)
    elif symbol=="/":
        print(num1/num2)
    elif symbol=="//":
        print(num1//num2)
    elif symbol=="%":
        print(num1%num2)
    elif symbol=="*":
        print(num1*num2)
    elif symbol=="**":
        print(num1**num2)
    else:
        print("invaild")

