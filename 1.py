def get_data (numberofnumbers):
    list=[]
    for i in range (numberofnumbers):
        add = input()
        list.append(add)
    return list
print("How many elements may your list have?")

amount=int(input())


print(get_data(amount))
