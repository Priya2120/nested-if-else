num=int(input("enter the number"))
a_num=(num%10)
b_num=(num//10)%10
c_num=(num//10)%10
fourth_num=(num//1000)%10
fifth_num=(num//10000)%10
reverse=(a_num*10000)+(b_num*1000)+(c_num*100)+(fourth_num*10)+(fifth_num*1)
if num>1000:
    print("reverse")
else:
    print("invaild")
