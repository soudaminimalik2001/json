import json
x={'name':'abhishek','designation':'ceo of navgurukul','gender':'male','age': 29}
with open("Json_file.json","w") as file:
    json.dump(x, file ,indent=5)
    print(x)









# {
#     “Name”: “Abhishek”,
#     “Designation”: “CEO of      navgurukul”,
#     “Gender”:”male”,
#     “Age”: “29”
#     }