s=input('enter sentence:')
w=s.split()
l=' '
c=0
for i in w:
    t=len(i)
    if c<t:
        c=t
        l=i
print(l)
print('length:',c)        

