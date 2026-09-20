transactions=[("Ali","deposit",50000000,10),("Ali","withdraw",2000000,11),("Ali","withdraw",3000000,12),("Ali","withdraw",4000000,13),\
              ("Ali","withdraw",5000000,14),("Ali","withdraw",6000000,15),("Sara","deposit",50000000,20),("Sara","withdraw",60000000,24),\
                  ("Reza","deposit",150000000,30)]
def check_large_transaction(transactions):
    suspicious=[]
    for i in transactions:
        if i[2]>100000000:
            suspicious.append(i)
    return suspicious
def check_repated_withdrawals(transactions):
    suspicious=[]
    last_withdraw_time={}
    withdraw_streak={}
    for i in transactions:
        name=i[0]
        action=i[1]
        time=i[3]
        if action=="withdraw":
            if name in last_withdraw_time and time -(last_withdraw_time[name])==1:
                withdraw_streak[name]+=1
                if withdraw_streak[name]>=3:
                    suspicious.append(i)
            else:
                withdraw_streak[name]=1
            last_withdraw_time[name]=time
    return suspicious
def check_balance(transactions):
    suspicious=[]
    balances={}
    for i in transactions:
        name=i[0]
        action=i[1]
        money=i[2]
        if name not in balances:
            balances[name]=0
        if action=="deposit":
            balances[name]+=money
        elif action=="withdraw":
            if money>balances[name]:
                suspicious.append(i)
            balances[name]-=money
    return suspicious
def  generate_fraud_report(transactions):
    report=[]
    report.extend(check_large_transaction(transactions))
    report.extend(check_repated_withdrawals(transactions))
    report.extend(check_balance(transactions))
    return report
def detect_fraud(transactions):
    report=generate_fraud_report(transactions)
    print("tarakonesh mashkok:")
    for i in report:
        print(i)
    return report
detect_fraud(transactions)    
       
       
        
        

