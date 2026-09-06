s=input('enter sentence:')
w=s.split()
count=0
word=' '
for i in w:
    t=w.count(i)
    if t>count:
        count=t
        word=i
        break
print(word, '-> ' ,count)        
        
    
    

