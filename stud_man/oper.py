from util import *

def registration(user,age,course,duration):
    data=read_json()
    stud_data={
        "sno":len(data["students"])+1,
        "user":user,
        'age':age,
        "course":course,
        "duration":duration
    }
    data["students"].append(stud_data)
    write_json(data)
    print(f"{user} registered succesfully ! ")

def update():
    pass

def delete_stud():
    pass