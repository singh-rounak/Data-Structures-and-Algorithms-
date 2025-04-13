'''  
If else statements can also be used with list comprehensions

'''

numbers = [num for num in range(1,11)]
print(numbers)

even_odd_list = ["Even" if i%2 == 0 else "Odd" for i in range(1,11)]
print(even_odd_list)

