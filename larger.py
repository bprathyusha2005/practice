# a=int(input("enter a value:"))
# b=int(input("enter b value:"))
# if a>b:
#     print("a is larger",a)
# else:
#     print("b is larger",b)    

# a=int(input("enter a value:"))
# b=int(input("enter b value:"))    
# c=int(input("enter c value:"))
# if a>b and a>c:
#     print("a is greater than b and c")
# elif b>a and b>c:
#     print("b is greater than a and c")
# elif c>a and c>b:
#     print("c is greater than a and b")        

data="HellosPython"
new=""
for i in range(len(data)):
    if i%2==0:
        new=new+data[i].upper()
    else:
        new=new+data[i]
print(new)            

   