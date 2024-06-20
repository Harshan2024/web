import json

def read_json(FILE="json/harshan.json"):
    try:
        with open(FILE) as f:
            
           return json.load(f)
    except:
        with open(FILE,"w") as f:
            data={
                "student":[]
            }    
            json.dump(data,f,indent=4)
        with open(FILE) as f:
            return  json.load(f)    
            
def write_json(data,FILE="json/harshan.json"):    
    with open(FILE,"w") as f:
           json.dump(data,f,indent=4)     
