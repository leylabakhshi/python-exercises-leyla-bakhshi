tasks={101:{
    "id":101,
    "title":"Fix login bug",
    "assignee":"Ali",
    "priority":"HIGH",
    "status":"OPEN"}
       ,102:{
           "id":102,
           "title":"Update API"
           ,"assignee":"Ali",
           "priority":"MEDIUM",
           "status":"IN_PROGRESS"}
       ,103:{
           "id":103,
           "title":"Write tests",
           "assignee":"Ali",
           "priority":"LOW",
           "status":"DONE"}}
def show_tasks():
    if not tasks:
        print("NO tasks found")
        return
    for task_id, task in tasks.items():
        print("ID:",task["id"])
        print("Title:",task["title"])
        print("Assignee:",task["assignee"])
        print("Priority:",task["priority"])
        print("Status:",task["status"])
        print("-"*30)
def create_task():
    try:
        task_id=int(input("Enter task id:"))
        if task_id in tasks:
            print("Error:ID already exists")
            return
        title=input("Enter title:").strip()
        assignee=input("Enter assignee").strip()
        priority=input("Enter priority(LOW|MEDIUM|HIGH)").strip().upper()
        status=input("Enter status(OPEN|IN_PROGRESS|DONE)").strip().upper()
        if  not title or not assignee:
            print("Error:Title and assignee are required")
            return
        if priority not in ["LOW","MEDIUM","HIGH"]:
            print("Error:Invalid priority")
            return
        if status not in ["OPEN","IN_PROGRESS","DONE"]:
            print("Error:Invalid status")
            return
        tasks[task_id]={"id":task_id,
                        "title":title,
                        "assignee":assignee,
                        "priority":priority,
                        "status":status}
        print("task created successfully")
    except ValueError:
        print("Error:ID must be a number")
def update_task():
    try:
        task_id=int(input("Enter task ID to update"))
        if task_id not in tasks:
            print("Error:Task not found")
            return
        task=tasks[task_id]
        title=input("New title (Enter to keep old):").strip()
        assignee=input("Newssignee (Enter to keep old):").strip()
        priority=input("New priority (LOW|MEDIUM|HIGH):").strip().upper()
        status=input("New status(OPEN|IN_PROGRESS|DONE):").strip().upper()
        if title:
            task["title"]=title
        if assignee:
            task["assignee"]=assignee
        if priority:
            task["priority"]=priority
        if status:
            task["status"]=status
        print("Task updated successfully ")
    except ValueError:
        print("Error :ID must be a number")
def delete_task():        
    try:
        task_id=int(input("Enter task ID to delete:"))
        if task_id not in tasks:
            print("Error :Task not found")
            return
        task=tasks[task_id]
        if task["status"]in["IN_PROGRESS","DONE"]:
            confrim=input("This task is in progress or done.delet?(yes|no):").strip().lower()
            if confrim != "yes":
                print("deletion cancelled")
                return
        del tasks[task_id]    
        print("Task deleted successfully")
    except ValueError:
        print("Error :ID must be a number")
def search_tasks():
    field=input("search by (assignee|priority|status):").strip().lower()
    if field not in ["assignee","priority","status"]:
        print("Error :Invalid search field")
        return
    value=input("Enter search value:").strip().upper()
    found=False
    print("\n--- natijeh jostojo---")
    for task in tasks.values():
        current_value=str(task[field]).upper()
        if current_value==value:
            print(task)
            found=True
    if not found:
        print("No matching tasks found")
def change_status():
    try:
        task_id=int(input("Enter task ID:"))
        if task_id not in tasks:
            print("Error:task not found")
            return
        task=tasks[task_id]
        old_status=task["status"]
        allowed={"OPEN":["IN_PROGRESS"],
                 "IN_PROGRESS":["DONE"],
                 "DONE":[]}
        new_status=input("Enter new status(OPEN|IN_PROGRESS|DONE):").strip().upper()
        if new_status not in ["OPEN","IN_PROGRESS","DONE"]:
            print("Error:Invalid status")
            return
        if new_status not in allowed[old_status]:
            print(f"Error:status transition not allower from {old_status}to {new_status}")
            return
        task["status"]=new_status
        print("status changed successfully")
    except ValueError:
        print("Error:ID must be a number")
def show_reports():
    total=len(tasks)
    done_count=0
    assignee_counts={}
    for task in tasks.values():
        if task["status"]=="DONE":
            done_count+=1
        assignee=task["assignee"]
        if assignee not in assignee_counts:
            assignee_counts[assignee]=0
        assignee_counts[assignee]+=1
    open_count=sum(1 for task in tasks.values()if task["status"]=="OPEN") 
    print("\n--- gozaresh giri---")
    print("Total tasks:",total)
    print("Completed tasks (DONE):",done_count)
    print("Open tasks (OPEN):",open_count)
    print("\nTask per assignee:")
    for assignee, count in assignee_counts.items():
        print(f"  {assignee}:{count}")
    if assignee_counts:
        most_busy=max(assignee_counts, key=assignee_counts.get)
        print(f"most_busy:{most_busy} with {assignee_counts[most_busy]}tasks")
def main():
    while True:
        print("\n---Task management system---")
        print("1.show tasks(Read)")
        print("2.creat task")
        print("3.update task" )
        print("4.Delete task" )
        print("5.search tasks")
        print("6.change status")
        print("7.show reports")
        print("0.Exit")
        choice=input("choose an option:")
        if choice=="1":
            show_tasks()
        elif choice=="2" :
            create_task()
        elif choice=="3":
            update_task()
        elif choice=="4":
            delete_task()
        elif choice=="5":
            search_tasks()
        elif choice=="6":
            change_status()
        elif choice=="7":
            show_reports()
        elif choice=="0":
            print("good bye")
            break
        else:
            print("Invalid choice try again")
main()
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
    


