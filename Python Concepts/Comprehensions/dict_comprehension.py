'''
DICTIONARY Comprehension
Syntax - dictionary = {key:value for variable in iterable}
'''

a = {num : num*num for num in range(1,11)}
print(a)

#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76

new_price = {key : value * dollar_to_pound for (key, value) in old_price.items()}

print(new_price)

#Adding if else condition 
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {key:value for (key,value) in original_dict.items() if value%2 == 0}
print(even_dict)

new_dict = {key:value for (key, value) in original_dict.items() if value%2 !=0 if value < 40}
print('new_dict = ',new_dict)