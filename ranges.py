count=0
for i in range(1,101):
    if i%2==0:
       count+=i
print(count)      



for i in range(1,101):
    if i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
    else:
        print(i)  


        
                  