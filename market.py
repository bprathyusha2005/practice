products=["milk","eggs","bread","butter","cheese"]
prices=[2.5,3.0,1.5,4.0,5.0]
stock=[10,20,15,8,5]
student={}
student["course"]="python"
print(student)
student["age"]=21
print(student)
print(student.items())
del student["course"]
print(student)
print(products)
print(prices)
print(stock)
print(len(products))
print(len(prices))
print(len(stock))
def display_products():
    for i in range(len(products)):
        print(f"{products[i]}-{prices[i]}-{stock[i]}")
def update_price(product_name,new_price):
    if product_name in products:
        index=products.index(product_name)
        prices[index]=new_price
        print(f"updated {product_name} to {new_price}")
    else:
        print("product not found") 
update_price("bread",2.0)
def stock_update(product_name,quantity):
    if product_name in products:
        index=products.index(product_name)
        stock[index]+=quantity
        print(f"updated stock {product_name} to {stock[index]}")
    else:
        print("stock not found")  
stock_update("milk",15)  
def search_product(product_name):
    if product_name in products:
        index=products.index(product_name)
        print(f"{product_name}-price:{prices[index]}-stock:{stock[index]}")
    else:
        print("product not found")                 
search_product("bread")
