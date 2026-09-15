students={"Ali":[18,17,20],"Sara":[15,19,18],"Reza":[12,14,10],"Mina":[20,20,19]}
best_name=""
best_avg=0
for i,j in students.items():
    total=sum(j)
    avg=total/len(j)
    print(i)
    print("avg:",round(avg,2))
    if avg>=15:
        print("status:Passed")
    else:
        print("status:Failed")
    if avg>best_avg:
        best_avg=avg
        best_name=i
print("best_name:",best_name)        

