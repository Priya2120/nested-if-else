print("welcome to atm")
card=input("insert a card")
if card=="debit card" or card=="atm card":
    print("transaction in process")
    language=input("select languade")
    if language=="english" or "hindi":
        print("inprocess")
        pin=int(input("enter your pin"))
        if pin==6789:
            print("please select transaction")
            transaction=input("transaction type")
            if transaction=="withdrawn":
                print("inprocess")
                amount=int(input("enter the amount"))
                if amount <=5000 :
                    print("in process")
                    account=input("enter a account")
                    if account=="saving account" or "current account":
                        print("in process")
                        print("transaction is successfully done")
                        print("collect your cash")
                        receipt=input("do you want reciept")
                        if receipt=="yes":
                            print("collect your reciept")
                            print("your remaining balance is",(5000-amount))
                            print("thank you for transaction")
            elif transaction=="pin change":
                 print("in process")
                 pin_change=(input("do you want to change pin"))
                 new_pin=int(input("enter your new pin"))
                 if pin_change=="yes":
                    print("your new pin is", new_pin)
            elif transaction=="deposit":
                print("select your bank")
                mobile_number=int(input("enter regester mobile number"))
                if mobile_number==9156286294:
                    print("in processing")
                    account_num==int(input("enter your account number"))
                    if account_num==1234567890:
                        print("transaction in process")
                        confirm=input=input("you are confirm for process")
                        if confirm=="yes":
                            print("enter you cash in machine")
                        else:
                            print("sorry")
            elif transaction=="balance inquiry":
                print("in process")
                account=input("select account")
                if account=="saving" or account=="current":
                    print("please wait")
                    print("your account balance is 5000")
                else:
                    print("as your wish. thank you")
            else:
                print("check transaction type")
        else:
            print("please check your pin")
    else:
        print("try again")
else:
    print("your card is not valid")


