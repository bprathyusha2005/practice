x=int(input("enter x value:"))
y=int(input("enter y value:"))
op=input("enter an operator:")
if op=='+':
    print(x+y)
elif op=='-':
    print(x-y)
elif op=='*':
    print(x*y)
elif op=='/':
    print(x/y)
elif op=='%':
    print(x%y)
elif op=='**':
    print(x**y)       
else:
    print("invalid operator")         