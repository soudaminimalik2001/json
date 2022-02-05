import json
d='{"a":1,"a":2,"a":3,"a":4,"b":1,"b":2}'
x=json.loads(d)
print(x)
# dict={}
# for i in x.items():
#     if i not in dict:
#         dict.update(i)
# print(d)
