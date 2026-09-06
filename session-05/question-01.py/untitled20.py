p=input('enter password:')
if len(p)<8:
    print('password must contain at least 8 characters')
if not any(i.isupper() for i in p):
    print('password must contain at least one uppercase letter')
if not any(i.islower() for i in p):
    print('password must contain at least one lowercase letter')
if not any (i.isdigit()for i in p):
    print('password must contain at least one number')
special='@#$%'
if not any(i in special for i in p):
    print('password must contain a special character(@,#,$,%)')
else:
    print('password is valid')    



