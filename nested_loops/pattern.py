 
# n = 5
# for i in range(n):
#     for j in range(n-1):
#         print("*",end=" ")
#     print(" ")

# for j in range(5,0,-1):
#         print("*",end=" ")


# ```python
# for j in range(5, 0, -1): 5 4 3 2 1
#     print("*", end=" ")
# ```

# ---

# ### Understanding `range(5, 0, -1)`

# `range(start, stop, step)`

# * start = 5
# * stop = 0 (❌ not included)
# * step = -1 (counts down)

# So the values of `j` will be:

# ```
# 5, 4, 3, 2, 1
# ```

# ---

# ### Trace Table

# | Iteration | Value of `j` | What gets printed |
# | --------- | ------------ | ----------------- |
# | 1         | 5            | `* `              |
# | 2         | 4            | `* `              |
# | 3         | 3            | `* `              |
# | 4         | 2            | `* `              |
# | 5         | 1            | `* `              |

# > `end=" "` means **print on the same line** with a space after each `*`.

# ---

# ### Final Output

# ```
# * * * * * 
# ```




# 1
# 2 2
# 3 3 3
# 4 4 4 4



# 1
# 1 2
# 1 2 3
# 1 2 3 4



for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    


for i in range(1,5):
    for j in range(i):
        print(i,end=" ")
    print()
    

