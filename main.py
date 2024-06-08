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
