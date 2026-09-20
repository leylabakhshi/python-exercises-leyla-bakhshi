def max_value(t):
    max_value=0
    best_key=""
    for key in t:
        if t[key]>max_value:
            max_value=t[key]
            best_key=key
    return best_key
def analyze_text(text):
    words=text.split()
    word_count=len(words)
    letters=0
    digits=0
    uppercase=0
    lowercase=0
    for i in text:
        if i.isalpha():
            letters+=1
            if i.isupper():
                uppercase+=1
            else:
                lowercase+=1
        elif i.isdigit():
            digits+=1
    letter_counts={}
    for i in text.lower():
        if i.isalpha():
           if i in letter_counts:
            letter_counts[i]+=1
        else:
            letter_counts[i]=1
    most_common_letter=max_value(letter_counts)
    word_counts={}
    for w in words:
        w_lower=w.lower()
        if w_lower in word_counts:
           word_counts[w_lower]+=1
        else:
           word_counts[w_lower]=1
    most_common_word=max_value(word_counts) 
    longest_word=words[0]
    shortest_word=words[0]
    for w in words:
        if len(w)>len(longest_word):
            longest_word=w
        if len(w)<len(shortest_word):
            shortest_word=w
    palindrome_words=[]
    for w in words:
        w_lower=w.lower()
        if w_lower==w_lower[::-1]:
         palindrome_words.append(w)
    result={"words":word_count,"letters":letters,"digits":digits,"most_common_letter":most_common_letter,"most_common_word":most_common_word,\
            "longest_word":longest_word,"shortest_word":shortest_word,"palindrome_words":palindrome_words,"uppercase":uppercase,"lowercase":lowercase} 
    return result
my_text="Hello word 123"
final_output=analyze_text(my_text)
print(final_output)
       
         
          
                   
                   
       
            
           
            
    
       
        
    

