products={"P01":("Laptop",1200,5),"P02":("Phone",800,0),"P03":("Tablet",500,12),"P04":("Mouse",50,25),"P05":("Keyboard",100,0)}
product_values={}
total_inventory_value=0
for i,j in products.items():
    name=j[0]
    price=j[1]
    stock=j[2]
    if stock>0:
        print("mojod:",name)
    else:
        print("na mojod:",name)
    value=price*stock
    product_values[name]=value
    total_inventory_value+=value
max_value=0
max_name=""
for i, j in product_values.items():
    if j >max_value:
        max_value=j
        max_name=i
print("بیشترین ارزش موجودی:",max_name,"باارزش:",max_value)
print("ارزش کل انبار:",total_inventory_value)        
     