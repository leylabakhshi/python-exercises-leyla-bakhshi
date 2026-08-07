num1=float(input('enter first number:'))
num2=float(input('enter scond number:'))
op=input('enter op (+,-,*,/):')
if op=='+':
    result=num1+num2
elif op=='-':
    result=num1-num2
elif op=='*' :
    result=num1*num2
elif op=="/":
    result=num1/num2
else:
    result='no find op'
print('result',result)
input('press enter to exit...')    
    


