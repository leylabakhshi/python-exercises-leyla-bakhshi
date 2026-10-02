def load_transactions():
    transactions=[]
    with open("C://Users//PENTiUM//Desktop//first//transactions.txt", "r")as f:
        for line in f:
            parts=line.strip().split(",")
            transactions.append(parts)
        return transactions
def calculate_balance():
    transactions=load_transactions()
    balances={}
    for t in transactions:
        name=t[0]
        action=t[1]
        amount=int(t[2])
        if name not in balances:
            balances[name]=0
        if action=="deposit":
            balances[name]+=amount
        elif action=="withdraw":
            balances[name]-=amount
def total_deposits():
    transactions=load_transactions()
    total=0
    for t in transactions:
        if t[1]=="deposit":
            total+=int(t[2])
    print("مجموع واریزها:",total)
    return total
def total_withdraw():
    transactions=load_transactions()
    total=0
    for t in transactions:
        if t[1]=="withdraw":
            total+=int(t[2])
    print("مجموع برداشت ها:",total)
    return total
def find_invalid_transactions():
    transactions=load_transactions()
    balances={}
    invalid=[]
    for t in transactions:
        name=t[0]
        action=t[1]
        amount=int(t[2])
        if name not in balances:
            balances[name]=0
        if action=="deposit":
            balances[name]+=amount
        elif action=="withdraw" :
            if amount>balances[name]:
                invalid.append(t)
            balances[name]-=amount
    print("تزاکنش های نامعتبر:",invalid)
    return invalid
def generate_report():
    transactions=load_transactions()
    report={}
    for t in transactions:
        name=t[0]
        action=t[1]
        amount=int(t[2])
        if name not in report:
            report[name]={"deposits":0,
                          "withdrawals":0,
                          "balance":0,
                          "invalid":[]
                          }
        if action=="deposit" :
            report[name]["deposits"]+=amount
            report[name]["balance"]+=amount
        elif action=="withdraw":
            report[name]["withdrawals"]+=amount
            if amount>report[name]["balance"]:
                report[name]["invalid"].append(t)
            report[name]["balance"]-=amount
    print("\n---گزارش نهایی---")
    for name, data in report.items():
        print(f"\nنام:{name}")
        print(f"مجموع واریز:{data["deposits"]}")
        print(f"مجموع برداشت:{data["withdrawals"]}")
        print(f"موجودی:{data["balance"]}")
        print(f"تراکنش نامعتبر:{data["invalid"]}")
    return report
generate_report()    
        
            
  
            
        
        
            
            
            
        
        
    

