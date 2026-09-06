s=input('enter :')
result=' '
count=1
for i in range(len(s)):
    if i+1<len(s)and s[i]==s[i+1]:
        count+=1
    else:
        if count>1:
            result+=s[i]+str(count)
        else:
            result+=s[i]
        count=1
print('result:',result)            


