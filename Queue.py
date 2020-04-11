'''# using python deque

from collections import deque
my_q = deque()
my_q.append(1)
my_q.append(2)
print(my_q)
print(my_q.popleft())
'''

# using class


class Queue:
    def __init__(self):
        self.qu = list()

    def enquess(self,num):
        self.qu.append(num)

    def deques(self):
        return self.qu.remove(self.qu[0])
    def __str__(self):
        return str(self.qu)


myQ = Queue()
myQ.enquess(10)
myQ.enquess(20)
myQ.enquess(30)
myQ.deques()
print(myQ)


