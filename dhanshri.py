a=int(input("enter first side"))
b=int(input("enter sec side"))
c=int(input("third side"))
if a==b==c:
    print("this triangle is equilateral")
elif a==b!=c or a==c!=b or a!=b==c:
    print("this triangle is isoscales")
else:
    print("this is scalen triangle")