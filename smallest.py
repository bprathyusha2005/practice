a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number"))
if a<b and a<c:
    print("a is smaller")
elif b<a and b<c:
    print("b is smaller")    
elif c<a and c<b:
    print("c is smaller")    
else:
    print("invalid")    