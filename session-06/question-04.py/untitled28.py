employees={"E01":{"name":"Ali","age":28,"salary":3000},"E02":{"name":"sara","age":32,"salary":4500},"E03":{"name":"Reza","age":25,"salary":2800}}
max_salary=0
max_name=""
for i,j in employees.items():
    if j["salary"]>max_salary:
        max_salary=j["salary"]
        max_name=j["name"]
print("max_salary:",max_name)
total=0        
for i,j in employees.items():
    total=total+j["salary"]
avg=total/len(employees)
print("avg:",avg)
for i,j in employees.items():
    if j["salary"]>3000:
        print(j["name"])
min_salary=999999
min_name="name" 
for i,j in employees.items():
    if j["salary"]<min_salary:
        min_salary=j["salary"]
        min_name=j["name"]
print("min_salary:",min_name)        
       
    
    
