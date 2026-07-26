# a="computer"
# new=""
# for ch in range(len(a)):  #0 1 2 3 4 5 6 7
#     if ch%2!=0:           #
#         #  print(a[ch]) 
#          new += a[ch].upper()
#     else:
#          new += a[ch]       
# print(new)

# s = "abc123@#"
# num_count=0
# alp_count =0
# spe=0
# for ch in s:
#     if ch.isalpha():
#         alp_count+=1
#     elif ch.isdigit():
#         num_count+=1
#     else:
#         spe+=1


# print("Alphabets count=",alp_count,"Numbers count=",num_count,"Special character count=:",spe)

# s="python123@"
# for ch in s:
#     if not ch.isdigit() and not ch.isalpha():
#         s  = s.replace(ch,"")
# print(s)

# x="python"
# rev=""
# for ch in x:
#     rev=ch+rev
# print(rev)    


# Given a string, reverse each word.
s = "hello world"
#step 1 : divide the strign into words using split
s = s.split(" ")

#step 2: use loop to itegearte each word
for i in range(len(s)):
    word = s[i] #hello 
    new = ""
    for ch in word:
        new = ch+new
    s[i] = new


final =""
for i in s:
    final +=i+" "
print(final)
