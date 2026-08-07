total=0
for i in range(1,11):
    if i%2==0:
        result=i+5
        print(i,'+5:',result)
    else:
        result=i*5
        print(i,'*5:',result)
        total=total+result
print('sum of all result:',total)
input('press enter to exit...')
    

