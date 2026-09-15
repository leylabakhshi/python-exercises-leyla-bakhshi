users=[("Ali",25,"Python"),("Sara",30,"Java"),("Reza",22,"Python"),("Mina",28,"c++"),("John",35,"Python"),("David",30,"Java")]
grops={}
lang_ages={}
lang_count={}
for i in users:
    name=i[0]
    age=i[1]
    lang=i[2]
    if lang in grops:
        grops[lang].append(name)
    else:
        grops[lang]=[name]
    if lang in lang_ages:
        lang_ages[lang]+=age
        lang_count[lang]+=1
    else:
         lang_ages[lang]=age
         lang_count[lang]=1
print(":گروه بندی کاربران:",grops)
print(":میانگین سن هر زبان")         
for i, j in lang_ages.items():
    avg=j/lang_count[i]
    print(i,":",round(avg,2))
print("مسن ترین کاربر هرزبان:")    
for i in grops:
    max_age=0
    maz_name=""
    for k in users:
        if k[2]==i:
            if k[1]>max_age:
                max_age=k[1]
                max_name=k[0]
    print(i,":",max_name)
max_lang="" 
max_count=0
for i, j in grops.items():
    if len(j)>max_count:
        max_count=len(j)
        max_lang=i
print("زبانی با بیشترین کاربر:",max_lang)
print("تمام زبان های موجود:",list(grops.keys()))        
          
    
    
         
        
        


