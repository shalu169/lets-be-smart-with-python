"""
This problem was asked by Stripe.
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{ "key": 3, "foo": { "a": 5, "bar": { "baz": 8 }}}
it should become:
{  "key": 3,  "foo.a": 5,  "foo.bar.baz": 8 }
You can assume keys do not contain dots in them, i.e. no clobbering will occur. """

a = eval(input())
d = {}
'''for i,j in a:
    if type(j)!=dict:
        d[i] = j
        a.pop(i)
    else:

'''
b = list(a.keys())
c = list(a.values())
d =[]
for i in c:



