import random
# a=random.randint(1,5)
# print(a)
# a=random.randrange(1,3)
# print(a)
# a=random.random()
# print(a)
# a=random.uniform(1,3)
# print(a)
# l1=[2,5,90,-5,89,12,56]
# a=random.choice(l1)
# print(a)
# l1=[2,5,90,-5,89,12,56]
# random.shuffle(l1)
# print(l1)


# import random
# x=random.randint(0,1)
# print(x)
# if x==0:
#     print("head")
# else:
#     print("tail")  



import random
names=input("enter names separed by comma:")
names_list=names.split(" ")
# person_selected=random.choice(names_list)
print(f"{random.choice(names_list)} will pay the bill")