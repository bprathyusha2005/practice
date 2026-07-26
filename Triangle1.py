s1=int(input("enter s1 value:"))
s2=int(input("enter s2 value:"))
s3=int(input("enter s3 value:"))
if s1==s2==s3:
    print("equilateral triangle")
elif s1==s2 and s2==s1 and s2!=s3 and s1!=s3:
    print("isosceles triangle")
elif s1!=s2 and s2!=s3 and s1!=s3:
    print("scalene triangle")                                                                                                    





        