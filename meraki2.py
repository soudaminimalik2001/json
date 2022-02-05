#o/p-{
    # "name": "David", 
    # "class": "I", 
    # "age": 6
# }
import json
d={"name":"david","class":"I","age":6}
with open("pinky.json","w")as file:
    json.dump(d,file,indent=4)
    print(d)