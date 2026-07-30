price=float(input('enter price:'))
if price>1000000:
      finalprice=price-(price*15/100)#15%
      print("finalprice:",finalprice)
elif price>500000:
      finalprice=price-(price*10/100)#10%
      print("finalprice:",finalprice)
else:
      finalprice=price
      print('finalprice:',finalprice)
input()
      
      
      