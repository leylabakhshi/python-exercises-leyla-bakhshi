s=input('enter string:')
letters=0
uppercase=0
lowercase=0
digits=0
spaces=0
special=0
for i in s:
    if i.isalpha():
        letters+=1
        if i.isupper():
            uppercase+=1
        else:
            lowercase+=1
    elif i.isdigit():
        digits+=1
    elif i==' ':
        spaces+=1
    else:
         special+=1
print('letters:',letters)
print('uppercase:',uppercase)
print('lowercase:',lowercase)
print('digits:',digits)
print('spaces:',spaces)
print('special:',special)
        
        
            
        
                
        
        

