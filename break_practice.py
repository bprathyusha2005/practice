# break is used when we want to stop the loop iteration imediately

# for i in range(1, 6):
#     if i == 3:
#         break
#     print(i)

# continue – Skip the current iteration
# continue skips the current loop iteration and moves to the next one.
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i) 

# num=[1,2,3,4,5,6] #carry on
# for i in num:
#     if i%2==0:
#         continue
#     print(i)

# num=[10,-5,3,-1,7]
# for i in num:
#     if i<0:
#         continue
#     print(i)

# num=[4,6,2,0,9,1]
# for i in num:
#     if i==0:
#         break
#     print(i)

# num=[3,5,7,9,11]
# for i in num:
#     if i<0:
#         continue
#         print(i)

# num=[5,-2,8,-1,0,9]
# for i in num:
#     if i<0:
#         continue
#     elif i==0:
#         break
#     else:
#         print(i)
#     print("hello")

# i = 1
# while i <=10:
#     print(i)
#     # i+=1

# x="python"
# rev=""
# for ch in x:
#     rev=ch+rev
# print(rev)

# s="welcome"
# count=0
# for ch in s:
#     count=count+1
# print("number of characters:",count)    


# x="PyThOn"
# y=x.upper()
# z=x.lower()
# print(y)
# print(z) 

# s="madam"
# rev=""
# for ch in s:
#     rev=ch+rev
# if s==rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")        

# s="python is easy"
# print(s.replace(" ","_"))

# s="computer"
# print(s[1::2])

# s="banana"
# print(s.count("a"))

# s="javascript"
# print(s.rfind("a"))

# s="12345"
# print(s.isdigit()) 

# s="python is very easy"
# a=len(s.split())
# print(a)

# s="banana apple mango"
# print(sorted(s))

# s="python is easy"
# old="easy"
# new="fun"
# print(s.replace("easy","fun"))

# s="radar"
# print(s[0])
# print(s[-1])
# if s[0]==s[-1]:
#     print("same character") 
# else:
#     print("not same")   


s="hello world"
print(s.replace(" ",""))
