day=input("enter the day")
if day=="thursday":
    print("its your holiday. you can go outside but with permission")
    outside=input("where you want to go")
    if outside=="market" or outside=="hospital":
        print("you are going to public place")
        permission=input("is disco give permission")
        if permission=="yes":
            print("you are permitted go outside")
            precaution=input("which precaution you take")
            if precaution=="mask and sanitizer":
                print("you can go but maintaing social distancing")
                time=float(input("what is your returning time"))
                if time<=6.00:
                    print("ok. you can go but take all precaution")
                    print("take bath after returning campus")
                else:
                    print("above give time. you need qurantine for day")
            else:
                print("with precaution you have to be in qurantine")
        else:
            print("your leave is rejected")
    else:
        print("if it is navgurukul work you dont need to quarantine but take saftey")
else:
    print("its not holiday. you are able to go outside if reason is must important")
    print("and you have to be in quarantine for some days")


