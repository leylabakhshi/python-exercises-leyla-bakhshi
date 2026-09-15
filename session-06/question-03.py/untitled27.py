t=input("enter reshteh:")
r={}
for i in t:
    if i.isalpha():
        if i in r:
            r[i]+=1
        else:
            r[i]=1
print(r)            

