inventory={"appel":20,"banana":5,"orange":0,"milk":12,"bread":0}
print("Available:")
for i,j in inventory.items():
    if j>0:
        print(i)
print("out of stock:")
for i,j in inventory.items():
    if j==0:
        print(i)
        
    

