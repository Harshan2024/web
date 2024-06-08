import json
def read_json():
    try:
        with open("json/harshan.json") as f:
            
           return json.load(f)
    except:
        with open("json/harshan.json","w") as f:
            data={
                "student":[]
            }    
            json.dump(data,f,indent=4)
        with open("json/harshan.json") as f:
            return  json.load(f)    
            
def write_json(data):    
    with open("json/harshan.json","w") as f:
           json.dump(data,f,indent=4)     
