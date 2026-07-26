height=int(input("what is your height?"))
bill=0
if height>=3:
    print("can ride")
    age=int(input("what is your age:"))
if age<12:
    bill=150
    print("ticket price is 150rs")
elif age<18:
    bill=250
    print("ticket price is 250rs")
else:
    bill=500
    print("ticket price is 500rs")  
    want_photo=input("Do you want to take photo(Y/N)?")
    if want_photo=='y' or want_photo=='Y':
        bill=bill+50
        print("your total bill is {bill}")
    else:
        print("can't ride")
print("bye")



size=input("what size pizza you want(S/M/L)? ")
bill=0
if size=='S' or size=='s':
    bill+=100
    print("small pizza price is 100 rs")
elif size=='M' or size=='m':
    bill+=200
    print("medium pizza price is 200 rs")
elif size=='L' or size=='l':
    bill+=200
    print("medium pizza price is 200rs")   
else:
    bill+=300
    print("large pizza price is 300rs")
    add_pepperoni=input("Do you want pepperoni(Y/N) ")
    if add_pepperoni=='Y' or add_pepperoni=='y':
        if size=='S' or size=='s':
            bill+=30
        else:
            bill+=50
    extra_cheese=input("Do you want extra cheese(Y/N)? ")
    if extra_cheese=='Y' or extra_cheese=='y':
        bill+=20
    print("your final bill is{bill}")           



name1=input("what is your name? ")
name2=input("what is his/her name? ")
combine_string=name1+name2
lower_case_string=combine_string.lower()
t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true=t+r+u+e
l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love=l+o+v+e
love_score=int(str(true))+int(str(love))
if love_score<10 or love_score>90:
    print(f"your score is {love_score} and you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"your score is {love_score} and you are alright together")
else:
    print(f"your love score is {love_score}")

