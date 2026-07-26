# has_ticket=bool(input("you have ticket or not:"))
# if has_ticket=="False":
#     print("not Allowed")
# else:
#     print("Allowed")
#     class_ticket=input("enter ticket class:")
#     if class_ticket=="A":
#         print("Belongs to class A")
#     elif class_ticket=="B":
#         print("Allowed to class B")
#     elif class_ticket=="C":
#         print("Allowed to class C")
#     else:
#         print("invalid ticket")




year=int(input("enter year:"))
if year%4==0 and year%100!=0:
    print("leap year")
else:
    print("non leap year")


weight=int(input("enter weight:"))
height=float(input("enter height:"))
BMI=weight/height*height
print(round(BMI,1))
if BMI<16.0:
    print("underweight(severe thinness)")
elif BMI>=16.0 and BMI<=16.9:
    print("underweight(Moderate thinness)")
elif BMI>=17.0 and BMI<=18.4:
    print("underweight(Mild thinness)")
elif BMI>=18.5 and BMI<=24.9:
    print("Normal range")
elif BMI>=25.0 and BMI<=29.9:
    print("overweight(pre-obese)")
elif BMI>=30.0 and BMI<=34.9:
    print("obese-class 1") 
elif BMI>=35.0 and BMI<=39.9:
    print("obese(class 2)")
elif BMI>=40.0:
    print("obese(class 3)")
else:
    print("invalid")    







