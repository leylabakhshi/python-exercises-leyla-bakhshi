sen1=input('enter sentence1:')
sen2=input('enter sentence2:')
w1=sen1.lower().split()
w2=sen2.lower().split()
common_words=[]
for i in w1:
    if i in w2 and i not in common_words:
        common_words.append(i)
print('common words:') 
for i in common_words:
    print(i)
       