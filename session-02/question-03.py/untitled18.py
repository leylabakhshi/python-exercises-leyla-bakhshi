fullname=input('enter firstname and lastname:')
space=fullname.find(" ")
firstname=fullname[0:space]
lastname=fullname[space:]
print("firstname:",firstname[0])
print('lastname:',lastname)
input()


