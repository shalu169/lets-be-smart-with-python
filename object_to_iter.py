#The __iter__() function returns an iterator for the given object (array, set, tuple etc. or custom objects).
#It creates an object that can be accessed one element at a time using __next__() function,
#which generally comes in handy when dealing with loops.
#iter(object)
#iter(callable, sentinel)
# Python code demonstrating
# basic use of iter()
#way 1:

listA = ['a', 'e', 'i', 'o', 'u']

iter_listA = iter(listA)
print(type(iter_listA))   #<class 'list_iterator'>

try:
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))  # StopIteration error
except:
    pass

# way 2:
# Python code demonstrating
# basic use of iter()
lst = [11, 22, 33, 44, 55]

iter_lst = iter(lst)
while True:
    try:
        print(iter_lst.__next__())
    except:
        break

# Way 3
# Python code demonstrating
# basic use of iter()

listB = ['Cat', 'Bat', 'Sat', 'Mat']

iter_listB = listB.__iter__()
print(type(iter_listB))
try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())  # StopIteration error
except:
    print(" \nThrowing 'StopIterationError'",
          "I cannot count more.")

# Way 4
# Python code showing use of iter() using OOPs

class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num - 1


# Driver code
if __name__ == '__main__':

    a, b = 2, 5

    c1 = Counter(a, b)
    c2 = Counter(a, b)

    # Way 1-to print the range without iter()
    print("Print the range without iter()")

    for i in c1:
        print("Eating more Pizzas, couting ", i, end="\n")

    print("\nPrint the range using iter()\n")

    # Way 2- using iter()
    obj = iter(c2)
    try:
        while True:  # Print till error raised
            print("Eating more Pizzas, couting ", next(obj))
    except:
        # when StopIteration raised, Print custom message
        print("\nDead on overfood, GAME OVER")
