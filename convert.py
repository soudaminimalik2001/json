# import json
# x='{"a":3,"b":"bat",4:4.6,"c":3}'
# y=json.load(x)
# print(y)




   
   
import json
f = open('data.json',)
data = json.load(f)
for i in data['emp_details']:
    print(i)
f.close()


\]







    # print(type(x))
# x={"a":3,"b":"bat",4:4.6,"c":3}
# y=json.dumps(x)
# print(y)
# print(type(y))
# x="soudamini"
# y=json.dumps(x)
# print(y)
# print(type(y))
# x=("apple","banana")
# y=json.dumps(x)
# print(y)
# print(type(y))
