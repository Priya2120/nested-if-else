held_class=int(input("enter the number classes held"))
attend_class=int(input("enter the number classes attende"))
if (held_class-attend_class)*100>=75:
    print("you are allowed to sit in exam")
else:
    print("sorry,you are not allowed.attend more classes from next time.")