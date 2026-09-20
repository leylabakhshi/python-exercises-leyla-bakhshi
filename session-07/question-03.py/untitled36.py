transactions=[("Ali","deposit",5000000),("Ali","withdraw",1000000),("Sara","deposit",8000000),("Ali","withdraw",500000),("Sara","withdraw",2000000),\
              ("Reza","deposit",10000000)]
def analyze_transactions(transactions):
    result={}
    for i in transactions:
        name=i[0]
        action=i[1]
        money=i[2]
        if name not in result:
            result[name]={"deposits":0,"withdrawals":0,"balance_change":0,"transactions":0}
        if action=="deposit":
            result[name]["deposits"]+=money
            result[name]["balance_change"]+=money
        elif  action=="withdraw":
            result[name]["withdrawals"]+=money
            result[name]["balance_change"]-=money
        result[name]["transactions"]+=1
    max_deposit_name=""
    max_deposit_money=0
    max_withdraw_name=""
    max_withdraw_money=0
    mast_active_name=""
    most_active_count=0
    for name, data in result.items():
        if data["deposits"]>max_deposit_money:
            max_deposit_money=data["deposits"]
            max_deposit_name=name
        if data["withdrawals"]>max_withdraw_money:
            max_withdraw_money=data["withdrawals"]
            max_withdraw_name=name
        if data["transactions"]>most_active_count:
            most_active_count=data["transactions"]
            most_active_name=name
    print("max_deposit:",max_deposit_name,"with money",max_deposit_money)
    print("max_withdraw:",max_withdraw_name,"with money",max_withdraw_money)
    print("most_active",most_active_name,"with",most_active_count)
    return result
output=analyze_transactions(transactions)
print(output)
 
       
            
            
            
            
            
    

