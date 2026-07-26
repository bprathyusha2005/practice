 
a  = "hello all good morning"
ls = a.split()
largest = ""
for i in ls:
    if len(i)>len(largest):
        largest = i

print("the largest word     ",largest, "     \nwith length",len(largest))
