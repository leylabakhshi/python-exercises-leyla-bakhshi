def get_values():
    n=int(input("تعداد مقادیر:"))
    values=[]
    for i in range(n):
        value=input()
        values.append(value)
    return values
def add_unique(unique_list, value,original_value):
    for item in unique_list:
        if item.lower()==value.lower():
            return False
    unique_list.append(original_value)
    return True
def process_values(values):
    unique_list=[]
    duplicate_count=0
    first_positions={}
    for i in range(len(values)):
        value=values[i]
        if value=="":
            print("       خالی وارد شد, نادیده گرفته میشود")
            continue
        is_new=add_unique(unique_list, value,value)
        if is_new:
            print(":مقدار جدید به لیست اضافه شد",value)
            first_positions[value.lower()]=i+1
        else:
            duplicate_count+=1
            position=first_positions.get(value.lower())
            print("مقدار تکراری ,اولین بار درموقعیت وارد شده است:",position,value)
    return unique_list,duplicate_count,first_positions
def show_report(unique_list,duplicate_count,first_positions):
    print(" \nگزارش نهایی:")
    print("مقادیر یکتا:",unique_list)
    print("تعداد مقاویر تکراری:",duplicate_count)
    print(  "تعداد مقادیر یکتا: ",len(unique_list))
    print(":موقعیت اوین ورود")
    for key, position in first_positions.items():
        print(" ",key.capitalize()," __>",position)
values=get_values()
unique_list,duplicate_count,first_positions=process_values(values)
show_report(unique_list,duplicate_count,first_positions)
    
            
    
    

