a={1,2,3,4,5}
b={10,11,12}
c={0,9}
a.add(10)
a.add((6,7,8))
print(a)
a.add([11,12])#error  we cant able to add list to set
print(a)
a.update({10,11,12})
a.update(b)  #we can also use |= for update ->a |=b
print(a)
a.pop()
print(a)
a.remove(4)
print(a)
a.discard(1)
print(a)
print(a.union(b))
print(a | b)
print(a | b | c)
print(a | (9,10))
print(a.union(b,c))
print(a.intersection(b))  #we can also perform intersection on more than two sets at a time as above in the union
print(a & b)
print(a.difference(b))
print(a.difference(b,c))
print(a.symmetric_difference(b)) #it is not allowed on multiple sets
print(a ^ b)
print(a ^ b ^ c)#this operator applicatle to multiple sets but not above sym diff method
print(a.isdisjoint(b))
print(a.issubset(b)) #use subset symbol also <=
print(a.issuperset(b)) #it is reverse of subset (use >= symbol for superset)
print(a.isdisjoint(10,11))
b.clear()
print(b)
del b
print(b)

