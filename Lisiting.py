shopping_list = ['apple', 'banana', 'mango', 'burger']
print(shopping_list)
print(shopping_list[0])
print(shopping_list[2])
print(shopping_list[3])

# slicing in list
print(shopping_list[0:1])
print(shopping_list[0:2])
print(shopping_list[0:3])
print(shopping_list[0:4])

# update in list
shopping_list.append('LemonMalt')
print(shopping_list)

shopping_list[0]='orange'
print(shopping_list)

del shopping_list[0]
print(shopping_list)

#length of list
print(len(shopping_list))

#combining lists
shopping_list2 = ['jam', 'mince','wings']
print(shopping_list2)
print(shopping_list+shopping_list2)

#repeating a list
print(shopping_list2*3)

#min and max
num_list = [1,8,5,3,6]
print(max(num_list))
print(min(num_list))