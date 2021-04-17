num=int(input("enter first side"))
num1=int(input("enter second side"))
num2=int(input("enter third side"))
if(num==num1==num2):
    print("it is an equilateral triangle")
elif(num==num1!=num2) or (num!=num1==num) or (num==num2!=num1):
    print("it is an isascales triangle")
else:
    print("it is scalen triangle")
