# num=[1,2,3,4,5]
# for i in num:
#     print(i)
# else:
#     print("successfully completed")    




# tuple1=(2,56,34,3,5,-1)
# for i in tuple1:
#     print(i)
#     if i==5:
#         break
# else:                           #here the else block is executed only if for loop is completed successfully
#     print("loop successfully completed and we are in else block now")        


# tuple1=(2,56,34,3,5,-1)
# for i in tuple1:
#     if i%6==0:
#         print(i)
#         break
# else:
#     print("there is no number divisible by 6 in this sequence!")



heights=input("enter all heights separated by space:")
height_list=heights.split()
print(height_list)
count=0
for height in height_list:
    count=count+1
print(count)    
for i in range(count):
    height_list[i]=int(height_list[i])
print(height_list)  
total=0
for person in height_list:
    total+=person
avg=total/count
print(round(avg))


numbers=input("enter the list of numbers:")
numbers_list=numbers.split()
print(numbers_list)
for i in range(6):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)


