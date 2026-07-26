# num=[1,4,6,7]
# for i in num:
#     print(i)

# for i in range(1,3):
#     print(i)
# for i in range(0,3,1):
#     print(i)


# L1=[1,2,3,4,5]
# count=0
# for i in L1:
#     count+=1
# print(count)

# a = "Hello world this is python. Today we are going to discussing about python"
# # convert_to_lowercase = a.lower()
# # print(convert_to_lowercase)

# split_sentences= a.split(".")
# print(split_sentences)

# st ="  hello  "
# print(len(st))
# x=st.strip()  # "hello"
# print(len(x))

# words = ["apple", "banana", "cherry"]
# # words[0]
# # print(words[0])
# # words[0].upper()
# # print(words[0].upper())
# for i in words:
#     i.upper()
#     print(i.upper())

# words = ["apple", "banana", "cherry"]
# for i in range(5): 
#     for j in range(i): 
#         print(j)
#     print("end")

# Let's break down the code you provided step by step. Here's the code:

# ```python
# for i in range(5): 
#     for j in range(i): 
#         print(j)
#     print("end")
# ```


# ### **Trace Output**:

# #### **First iteration (i = 0)**:

# * The outer loop starts with `i = 0`.
# * The inner loop runs `range(0)`, which means it doesn't run at all.
# * Then, the statement `print("end")` is executed, so we print:

#   ```
#   end
#   ```

# #### **Second iteration (i = 1)**:

# * The outer loop moves to `i = 1`.
# * The inner loop runs `range(1)`, meaning `j` takes the value 0 once.

#   * So, `print(j)` is called and prints `0`.
# * Then, the statement `print("end")` is executed, so we print:

#   ```
#   0
#   end
#   ```

# #### **Third iteration (i = 2)**:

# * The outer loop moves to `i = 2`.
# * The inner loop runs `range(2)`, meaning `j` will take the values 0 and 1.

#   * First, `print(j)` prints `0`.
#   * Then, `print(j)` prints `1`.
# * Then, the statement `print("end")` is executed, so we print:

#   ```
#   0
#   1
#   end
#   ```

# #### **Fourth iteration (i = 3)**:

# * The outer loop moves to `i = 3`.
# * The inner loop runs `range(3)`, meaning `j` will take the values 0, 1, and 2.

#   * First, `print(j)` prints `0`.
#   * Then, `print(j)` prints `1`.
#   * Finally, `print(j)` prints `2`.
# * Then, the statement `print("end")` is executed, so we print:

#   ```
#   0
#   1
#   2
#   end
#   ```

# #### **Fifth iteration (i = 4)**:

# * The outer loop moves to `i = 4`.
# * The inner loop runs `range(4)`, meaning `j` will take the values 0, 1, 2, and 3.

#   * First, `print(j)` prints `0`.
#   * Then, `print(j)` prints `1`.
#   * Then, `print(j)` prints `2`.
#   * Finally, `print(j)` prints `3`.
# * Then, the statement `print("end")` is executed, so we print:

#   ```
#   0
#   1
#   2
#   3
#   end
#   ```

# ---

# ### **Final Output**:

# Here’s the **complete output** of the code:

# ```
# end
# 0
# end
# 0
# 1
# end
# 0
# 1
# 2
# end
# 0
# 1
# 2
# 3
# end
# ```

# ### **Explanation**:

# * The **outer loop** (`for i in range(5)`) runs 5 times, with `i` taking values from 0 to 4.
# * The **inner loop** (`for j in range(i)`) runs `i` times. So, for each iteration of the outer loop:

#   * When `i = 0`, the inner loop doesn't run at all.
#   * When `i = 1`, the inner loop runs once (prints `0`).
#   * When `i = 2`, the inner loop runs twice (prints `0`, `1`).
#   * When `i = 3`, the inner loop runs three times (prints `0`, `1`, `2`).
#   * When `i = 4`, the inner loop runs four times (prints `0`, `1`, `2`, `3`).


# box = ["apple", "banana", "cherry"]

# for fruit in box:
#     for cut in fruit:
#         print(cut)
#     print(" ")    

# x=["ALICE","BOB","CHARLIE"]
# for i in x:
#     for j in i:
#         y=j.lower()
#         print(y)
#     print("")    

# items=["  pen","  book "," pencil  "]
# for i in items:
#       x=i.strip()
#       print(x) 

# sentence="I love learning python"
# for i in sentence.split():
#     print(i)
#     y=len(i)
# print("this sentence contains",y,"words")

# x="   PYTHON IS FUN"
# a=x.strip()
# print(a)
# b=a.lower()
# print(b)
# c=b.split()
# for word in c:
#     print(word)       
 
x="cherry"
print(x[::-1])
