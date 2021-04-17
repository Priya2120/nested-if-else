gmail=input("enter a gmail or mobile number")
password=input("enter a passward")
if gmail=="priya123@gmail.com" or "9156286294":
    if password=="payal":
        print("login to your account")
    else:
        print("forget password")
        mobile=int(input("enter your mobile number"))
        if mobile=="9156286294":
            print("checking your account")
            new_passward=input("enter your new passward")
            print("your new passward is",new_passward)
        else:
            print("your number is not vaild")
else:
    print("give gmail not vaild")