print("welcome")
card=input("insert the card")
if card=="debit card":
    print("transactor is in process")
    language=input("select the language")
    if language == "english":
        print("inprocess")
        pin=int(input("Enter your 4 digit pin "))
        if pin == 1234: 
            print("inprocess")
            account = input("type of account")
            if account == "saving account" or account=="current accont":
                print("inprocess")
                amount=int(input("enter the amount to be widroll"))
                if amount<=50000:
                    print(10000-amount,"transaction is in process") 
                    print("please collect your cash")
                    recept=input("do you want to take recept")
                    if recept=="yes":
                        print("take the recept")
                        print("thanku")
                    else:
                        print("ok good iuck")
                        print("thank you for banking with us")
                else:
                    print("please enter the correct amount")
            else:
                print("please enter the correct account")
        else:
            print("try again pin")
    else:
        print("your language is incorrect")
else:
    print("please enter the correct amount")
                    

        
    

   
