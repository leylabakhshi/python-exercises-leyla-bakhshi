s=input('enter matn:')
w=s.lower().split()
k=['hack','fraud','scam','password','attack']
for i in k:
    t=w.count(i)
    if 0<t:
        print(t,'<-',i)
        

