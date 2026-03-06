'''lst = [1,2,3,4,5]
res = []
for i in lst:
    res.append(i**2)
print(res)
ans = [i**2 for i in lst]
print(ans)

lst = [1,2,3,4,5]
res = []
for i in lst:
    if i%2==0:
        res.append(i)
print(res)
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
'''
n = 4
for i in range(1,n+1):
    print(" "*n-i)
