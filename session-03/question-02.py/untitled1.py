onenumber=0
for i in range(10):
    height=float(input('enter jump height (meter):'))
    if i==0:
        onenumber=height
        print('first record save max number:',onenumber)
    else:
        if height>onenumber:
            onenumber=height
            print('new record max height:',onenumber)
        else:
            print ('not record max height:',onenumber)
input('press enter to exit...')            

