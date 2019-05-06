def get_data (numberofnumbers): #this function recives the size of list and then let user to add numbers as its elements
    list=[]
    for i in range (numberofnumbers):
        add = input()
        list.append(add)
    return list
print("How many elements may your list have?") #asking user to insert list size

amount=int(input())


print(get_data(amount)) #requesting created function
print("change")
