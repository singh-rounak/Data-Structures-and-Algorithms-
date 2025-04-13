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

new_dict1 = {key: ('old' if value > 40 else 'young') for (key,value) in original_dict.items()}
print(new_dict1)

dict = {k1:{k2: k1*k2 for k2 in range(1,6)} for k1 in range(2,5)}
print(dict)
#Note - when nested loops are used, Python first executes outer loop then inner loop.

#The above can also be broken down as:
dict1 = {}
for k1 in range(2,5):
    dict1[k1] = {k2:k2*k1 for k2 in range(1,6)} 

print(dict1)

Hmap = {}
for k1 in range(2,5):
    Hmap[k1] = {}
    for k2 in range(1,6):
        Hmap[k1][k2] = k1*k2

print(Hmap)

# First for loop execution output looks like this - 
# Hamp = {2:{}, 3:{}, 4:{}}

# Second for loop execution output looks like this separately -
# hmap[2] - {1:2, 2:4, 3:6 ,4:8, 5:10}
# hmap[3] - {1:3, 2:6, 3:9, 4:12, 5:15}
# hmap[4] - {1:4, 2:8, 3:12, 4:16, 5:20}

#combine both - 
# Hmap = {2:{1:2, 2:4, 3:6 ,4:8, 5:10}, 3:{1:3, 2:6, 3:9, 4:12, 5:15}, 4:{1:4, 2:8, 3:12, 4:16, 5:20}}

print(dict == dict1 == Hmap)
#True
