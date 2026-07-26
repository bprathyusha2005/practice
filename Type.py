# x=int(input("enter 1st number:"))
# y=int(input("enter 2nd number:"))
# if x<0 and y<0:
#     print("both are negative")
# elif x>0 and y>0:
#     print("both are positive")
# elif x<0 and y>0 or x>0 and y<0:
#     print("mixed")
# else:
#     print("invalid")     
# 
       
# x=input("enter an alphabet:")
# if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
#     print("vowel")
# else:
#     print("consonant")

# s="education"
# count=0
# for ch in s:
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#         count+=1
# print(count)    

#2nd way
# s="Education"
# count=0
# for ch in s:
#     ch = ch.lower()
#     if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
#         count+=1
# print(count)    

# 3nd way

# s="Education"
# count=0
# list = ['a','e','i','o','u']
# for ch in s:
#     if ch in list:
#         count+=1
# print(count)    

s="computer"
print(s[::2])