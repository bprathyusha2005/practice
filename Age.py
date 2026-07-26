x=int(input("enter age:"))
if x>=0 and x<=12:
    print("child")
elif x>=13 and x<=19:
    print("teenage")
elif x>=20 and x<=59:
    print("Adult")
elif x>=60:
    print("senior")
else:
    print("invalid")
                     