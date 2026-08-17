password=input('enter password:')
if len(password)==8 and password[:4].isalpha()\
    and password[4:].isdigit():
        print('motabar')
else:
        print('na motabar')
input('press enter to exit...')        

