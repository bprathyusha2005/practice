x=int(input("enter x number:"))
y=int(input("enter y value"))
z=int(input("enter z value"))
if x+y>z and y+z>x and x+z>y:
    print("Forms a valid triangle")
else:
    print("invalid triangle")    