# generator function
def generator_function():
    yield 2
    yield 3
    yield 4
# way 1
print(generator_function())  #this is an generator function
count = 0
for i in generator_function():
    count += 1
    print(i)     # print
print('no of time loop executes', count)  # 3 times loop executes
# every time function is called 1 yield executes
#way 2 :make a generator object
x = generator_function()
print(next(x))
print(x.__next__())
print(x.__next__())
#print(x.__next__())

