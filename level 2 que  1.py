age=int(input("enter age"))
sex=input("sex?(m or f)")
marry=input("marry?(yes or no)")
if sex == "f" and age>=20 and age<=60:
    print("urban areas only")
elif sex == "m" and age>=20 and age<=40:
    print("any where")
elif sex=="m" and age>=40 and age<=60:
    print("work only in urban area")
else:
    print("ERROR")