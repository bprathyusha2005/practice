# num=int(input("enter a number:"))
# if num%4==0:
#     print("leap year")
# else:
#     print("Not a leap year")    




year=int(input("enter year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:    
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")        