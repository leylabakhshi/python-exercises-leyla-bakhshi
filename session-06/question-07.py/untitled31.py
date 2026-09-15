orders=[("Ali","Laptop"),("Sara","Phon"),("Ali","Phone"),("Reza","laptop"),("Sara","Laptop"),("Ali","Tablet"),("Reza","Phone")]
r={}
for i in orders:
    customer=i[0]
    product=i[1]
    if customer in r:
        r[customer].append(product)
    else:
        r[customer]=[product]
print(r)        
        
        
                                                          
                                                          

