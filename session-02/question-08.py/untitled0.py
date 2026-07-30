zaman=int(input('enter clock:'))
if 0<=zaman<=3:
    print('midnight:')
elif 4<=zaman<=11:
    print('morning:')
elif 12<=zaman<=14:
    print('noon:')
elif 15<=zaman<=19:
    print('afternoon:')
elif 20<=zaman<=23:
    print('night:')
else:
     print('unknown clock:')
input()     
   

