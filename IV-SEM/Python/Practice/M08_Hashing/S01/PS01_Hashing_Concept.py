'''
Hashing:
Advantages:

a = 20
b = 'Nikhil'
c = 35.55
print(hash(a))
print(hash(b))
print(hash(c))'''
size=7
table=[None]*size
a=[10,20,30]
for key in a:
    index=key%size
    table[index]=key
print(table)