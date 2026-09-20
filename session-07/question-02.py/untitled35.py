def process_order(customer,*products,**options):
    discount=options.get("discount",0)
    tax=options.get("tax",0)
    shipping=options.get("shipping",0)
    base_price=len(products)*1000
    final_price=base_price-discount+tax+shipping
    result={"customer":customer,"products":list(products),"discount":discount,"tax":tax,"shipping":shipping,\
            "final_price":final_price}
    return result
result=process_order("Ali","Laptop","mouse","keyboard",discount=10,tax=9,shipping=200000)
print(result)    

