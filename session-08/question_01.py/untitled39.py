def load_users():
    users=[]
    with open(r"C://Users//PENTiUM//Desktop//first//users.txt", "r") as f:
        for line in f:
            t=line.strip().split(",")
            users.append(t)
    return users
def save_users(users):
    with open(r"C://Users//PENTiUM//Desktop//first//users.txt", "w") as f:
        for user in users:
            line=",".join(user)
            f.write(line+"\n")
def add_user(username, password):
    users=load_users()
    for user in users:
        if user[0]==username:
            print("این کاربر قبلا وجود داره")
            return
    users.append([username, password,"active"])
    save_users(users)
    print("کاربر با موفقیت اضافه شد")
def find_user(username):
    users=load_users()
    for user in users:
        if user[0]==username:
          print("کاربر بود",user)
          return user
    print("کاربر نبود")
    return None
def delet_user(username):
    users=load_users()
    for i in range(len(users)):
        if users[i][0]==username:
            del users[i]
            save_users(users)
            print("کاربر با موفقیت حذف شد")
            return
    print("کاربر یافت نشد")
def generate_report():
    users=load_users()
    active_count=0
    blocked_count=0
    for user in users:
        if user[2]=="active":
            active_count+=1
        elif user[2]=="blocked":
            blocked_count+=1
    print("active_count:",active_count) 
    print("blocked_count:",blocked_count)
add_user("Hasan","112233")
find_user("Sara") 
delet_user("Reza")
generate_report()
print(load_users())   
    
    
            
            
        
        
    
        
    
         
        
        
    


