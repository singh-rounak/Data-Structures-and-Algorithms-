from Implementation import Stack

s = Stack()

'''
Perform the following Operations:
Implement the Stack class as above.
Push a series of integers onto the stack.
Pop all elements one by one and display the state of the stack after each operation.
Try to pop from an empty stack and see what happens.
'''

print(s) 
s.push(10)
s.push(20)
s.push(30)
s.push(50)


s.pop()
s.display()