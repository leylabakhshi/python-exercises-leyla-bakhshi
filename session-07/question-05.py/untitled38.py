logs=[("Ali","LOGIN",200),("Ali","DOWNLOD",200),("Sara","LOGIN",403),("Reza","LOGIN",200),("Sara","LOGIN",403),("Sara","LOGIN",403)]
def analyze_logs(logs):
    login_success_count=0
    login_fail_count=0
    fail_user={}
    activity_user={}
    
    for i in logs:
        name=i[0]
        action=i[1]
        code=i[2]
        if name in activity_user:
            activity_user[name]+=1
        else:
            activity_user[name]=1
        if code==200:
            login_success_count+=1
        elif code==403:
            login_fail_count+=1
            if name in fail_user:
                fail_user[name]+=1
            else:
                fail_user[name]=1    
    suspicious_user=[]
    for i, j in fail_user.items():
          if j>=3:
              suspicious_user.append(i)
    report={"login_success":login_success_count,"login_fail":login_fail_count,"activity_user":activity_user,\
        "suspicious_user":suspicious_user,"fail_user":fail_user}
    return report
result=analyze_logs(logs)
print(result)

              
              
          
            



