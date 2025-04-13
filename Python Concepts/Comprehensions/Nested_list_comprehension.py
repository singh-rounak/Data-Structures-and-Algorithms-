'''
NESTED LIST COMPREHENSIONS
Mostly used with 2D arrays while problem solving - eg: matrix or island
'''
multiply = [[i *j for j in range(1,6)] for i in range (1,6)]
print(multiply)

print(type(multiply))

rows = len(multiply)
cols = len(multiply[0])

print(f'Dimensions = {rows}x{cols}')