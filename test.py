s = input()
li = s.split()
print(li)
l2=[]
for a in li:
    print(a)
    if(a[0]>='a' and a[0] <= 'z'):
        print(a[0])
        a = a[0].upper()+a[1:]
        print(a)
    l2.append(a)    #a[0].upper()
print(l2)
s = ' '.join(l2)
#    return s
print(s)