sales=(("Ali","Laptop",1200),("Sara","Phone",800),("Ali","Phone",800),("Reza","Laptop",1200),("Sara","Laptop",1200),("Ali","Mouse",50))
customer_totals={}
product_counts={}
total_sales=0
for i in sales:
    customer=i[0]
    product=i[1]
    price=i[2]
    if customer in customer_totals:
        customer_totals[customer]+=price
    else:
        customer_totals[customer]=price
    if product in product_counts:
        product_counts[product]+=1
    else:
        product_counts[product]=1
    total_sales+=price
print("customer_totals:")
for i,j in customer_totals.items() :
    print(i,":",j)
print("product_counts:")
for i,j in product_counts.items():
    print(i,":",j)
print("total_sales:",total_sales)    
    

