username=input('create your username:')
password=input('create your password:')
attempts=3
while attempts>0:
    user=input('enter username:')
    passw=input('enter password:')
    if user==username and passw==password:
        print('login successfull')
        break
    else:
        attempts=attempts-1
        if attempts==0:
            print('wrong username or password')
            print('attempts remaining:0')
            print('account locked')
        else:
            print('wrong username or password')
            print('attempts remaining:',attempts)
            
            


