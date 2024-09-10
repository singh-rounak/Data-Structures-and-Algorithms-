class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack.is_empty():
            print('Stack is empty')
        item = self.stack.pop()
        return item

    def peek(self):
        if self.stack.is_empty():
            print('Stack is empty')
        else:
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack
