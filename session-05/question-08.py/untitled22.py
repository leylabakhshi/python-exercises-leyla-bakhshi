s=input('enter text:')
w=s.split()
total_characters=len(s)
total_word=len(w)
total_spaces=s.count('')
total_digits=sum(i.isdigit()for i in s)
total_letters=sum(i.isalpha() for i in s)
total_uppercase=sum(i.isupper()for i in s)
total_lowercase=sum(i.islower()for i in s)
longest_word=''
for word in w:
    if len(word)>len(longest_word):
        longest_word=word
shortest_word=w[0] 
for word in w:
    if len(word)<len(shortest_word):
        shortest_word=word
char_count={} 
for i in s:
    if i !=' ':
        if i in char_count:
            char_count[i]=char_count[i]+1
        else:
            char_count[i]=1
most_char=''
max_char=0
for i in char_count:
    if char_count[i]>max_char:
        max_char=char_count[i]
        most_char=i
word_count={} 
for word in w:
    if word in word_count:
        word_count[word]=word_count[word]+1
    else:
        word_count[word]=1
most_word=''
max_word=0
for word in word_count:
    if word_count[word]>max_word:
        max_word=word_count[word]
        most_word=word
print('total characters:',total_characters)
print('total letters:',total_letters)
print('total word:',total_word)
print('total digits:',total_digits)
print('total spaces:',total_spaces) 
print('total uppercase:',total_uppercase)
print('total lowercase:',total_lowercase) 
print('longest word:',longest_word) 
print('shortest word:',shortest_word)
print('most repeated charcater:',most_char,'->',max_char)
print('most repeated word:',most_word,'->',max_word)
    
    
        
        
       
        
        
       
       

