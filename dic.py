dic={"name":"prathyu","roll_no":20,"sec":"A"}
for i in dic.values():
    print(i)
for i in dic.keys():
    print(i)    
for i in dic.items():
    print(i)   
for i,j in {"name":"prathyu","roll_no":20,"sec":"A"}.items():
    print(i,j)
print(dic.keys())
print(dic.values())
print(dic.items())
dic.pop("name")
print(dic)
dic.clear()
print(dic)
print(dic.get("name"))
print(dic.get("roll_no"))
print(dic.get("sec"))
dic.update({"address":"anantapur"})
print(dic)