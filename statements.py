height=int(input("enter height in feet:"))
if(height>3):
    print("Buy Token")
else:
    print("no token required")    


a=int(input("enter a number:"))
if a%2==0:
    print("even")
else:
    print("odd")  




#nested if else
height=int(input("what is your height in feet:"))
if height>3:
    print("you can ride")
    age=int(input("what is your age:"))
    if age<=18:
        print("pay 250 rupees") 
    else:
        print("pay 300 rupees") 
else:
    print("cannot ride")              
          