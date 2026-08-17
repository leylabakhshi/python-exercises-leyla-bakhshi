import random
r=['sang','kaghaz','gheychi']
while True:
    s=input('sang,kaghaz, ya gheychi')
    if s=='exit':
        print('bazi tamom shod')
        break
    if s not in r:
        print('vorodi eshtebah')
        continue
    computer=random.choice(r)
    print('computer:',computer)
    if s==computer:
        print('mosavi')
    elif (s=='sang'and computer=='gheychi'or\
          s=='kaghaz'and computer=='sang'or\
              s=='gheychi'and computer=='kaghaz' ):
        print('barandeh shodid')
    else:
        print('computer barandeh shod')
input('press enter to exit...')        
        
    

