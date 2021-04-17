age1=int(input("enter first age"))
age2=int(input("enter second age"))
age3=int(input("enter third age"))
if age1>age2 and age1>age3:
    print("oldest",age1)
elif age2>age1 and age2>age3:
    print("oldest",age2)
elif age3>age1 and age3>age2:
    print("oldest",age3)
else:
    print("all are equal") 