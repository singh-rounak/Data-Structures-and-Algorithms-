'''
LIST COMPREHESIONS IN PYTHON

syntax : [expression for item in list if condition == True]
The 'if' condition is optional.

Why are list comprehensions extensively used?
-> List comprehensions are used to make the code clear and concise by eliminating 'for' loops
-> Can create lists from scratch
-> Can be used to create new lists from existing lists

'''

nums = [1,2,3,4,5,6,7,8,9,10]
print("Nums = ", nums)
# my_list = []
# for num in nums:
#   my_list.append(num)

# print(my_list)

#List comprehension for creating a list with doubled numbers:
a = [2 * num for num in nums]
print('a = ', a)

b = [2 + num for num in nums]
print('b = ', b)

new_list =[1,2,-3,4]
doubled_positive_only = [num *2 for num in new_list if num > 0]

print('new list = ',new_list)
print('output = ' , doubled_positive_only)

squared_numbers = [num*num for num in new_list]
print('squared = ', squared_numbers)

# #Even numbers only

even_only = [num for num in nums if num%2 == 0]
print('even_only = ', even_only)

#Range
subset = [num for num in range(5)]
print('subset=',subset)

odd_subset = [num for num in range(5) if num %2 !=0]
print("Odd subset = ", odd_subset)

# even_subset = [num for num in range(5,10) if num %2 ==0]
# print("Even subset = ", even_subset)

get_in_range = [i for i in range(5,9)]
print(get_in_range)
print(range(10))


