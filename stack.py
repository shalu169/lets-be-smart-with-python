# stack using class and objects:

class Stack:
    def __init__(self):
        self.stack = []

    def push(self,num):
        self.stack.append(num)

    def pop(self):
        if len(self.stack)==0:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1]
    def __str__(self):
        return str(self.stack)
my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
print(my_stack)
print(my_stack.pop())
print(my_stack.peek())
print(my_stack)




