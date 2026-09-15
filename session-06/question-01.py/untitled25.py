products={"laptop":1200,"phon":800,"tablet":500,"headphon":150,"mouse":50}
expensive=max(products,key=products.get)
print("expensive:",expensive)
cheap=min(products,key=products.get)
print("cheap:",cheap)
total=sum(products.values())
count=len(products)
avg=total/count
print("avg:",avg)
for name,price in products.items():
    if price>500:
        print(name,price)
print("total:",total)        
    


