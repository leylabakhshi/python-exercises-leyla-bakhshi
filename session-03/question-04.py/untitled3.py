e=input('enter text:')
s=len(e)
half=s//2
if s%2==0:
    print(e[:half])
else:
    print(e[half:]) 
input('press enter to exit...')    