list=["neelam","programer","24","2400"]
list1=["komal","trainer","24","20000"]
list2=["anuradha","HR","25","40000"]
list3=["Abhishek","manager","29","63000"]
a=["name","designation","age","salary"]
b=["emp1","emp2","emp3","emp4"]
#  dict={}
#  dict1={}
# dict2={}
# dict3={}
# dict4={}
# for i in range(len(list)):
#     dict["name"]=[list[i]]
#     dict["designation"]=[list[i]]
#     dict["age"]=[list[i]]
#     dict["salary"]=list[i]
#     print(dict)
    # print(dict1)
    # print(dict2)
    # print(dict3)
x=dict(zip(a,list))
# print(x)
y=dict(zip(a,list1))
# print(y)
z=dict(zip(a,list2))
# print(z)
s=dict(zip(a,list3))
# print(s)
dict1={}
j=0
for i in x,y,z,s:
    dict1[b[j]]=i
    j+=1
print(dict1)
