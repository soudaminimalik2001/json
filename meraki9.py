shopping_list={"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20"}
key=input("enter key")
value=int(input("enter value"))
for i in shopping_list:
    if i==key:
        if shopping_list[i]==value:
            a=int(shopping_list[i])
            b=a-value
            print(b)
            
