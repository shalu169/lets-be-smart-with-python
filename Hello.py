#Introduction to python
'''print('hello all this is testing file')
a = input("enter values")
print(a) #string
a,b = input("enter values").split()
print(a,b) #string
print("First number is {} and second number is {}".format(a, b)) #another way to print
x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)
'''
#list comprehension
#x, y = [int(x) for x in input("Enter two value: ").split()]
#print(x,y,type(x))
#x, y, z = [int(x) for x in input("Enter three value: ").split()]
x = [int(x) for x in input("Enter multiple value: ").split()]
print("Number of list is: ", x) #Number of list is:  [1, 2, 3, 4, 5]
# code for disabling the softspace feature
print('G', 'F', 'G', sep='')  #GFG

# for formatting a date
print('09', '12', '2016', sep='-') #09-12-2016

# another example
print('pratik', 'geeksforgeeks', sep='@') #pratik@geeksforgeeks
print('G', 'F', sep='', end='')  #GFG
print('G')
# \n provides new line after printing the year
print('09', '12', sep='-', end='-2016\n') #09-12-2016

print('prtk', 'agarwal', sep='', end='@')  #prtkagarwal@geeksforgeeks
print('geeksforgeeks')