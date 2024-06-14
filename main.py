from utils import*

def student_registration(Name,Age,Course,Duration):
    data=read_json()
    stud={
        "sno":len(data["student"])+1,
        "Name":Name,
        "age":Age,
        "course":Course,
        "course_Duration":Duration    
    }
    data["student"].append(stud)    
    write_json(data)
    
def delete_stud(id):
    data=read_json()
    name=""
    for i in data["student"]:
        if i["sno"]==id:
            name=i["Name"]
            data["student"].remove(i)
    a=1
    for b in data["student"]:
        b["sno"]=a     
        a+=1
        
    write_json(data)        
    return name    

def update_stud(id,Name,Age,Course,Duration):
    data=read_json()
    for i in data["student"]:
        if i["sno"]==int(id):
            i["Name"]=Name
            i["age"]=Age
            i["course"]=Course
            i["course_Duration"]=Duration
    write_json(data)
            
            
        
    
            
            
    
    
