''' 
li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i**2)
print(res)
ans = [i**2 for i in li] 
print(ans)
'''
'''
li = [1,2,3,4,5]
res = []
for i in li:
    res.append(i)
print(res)
print([i for i in li if i%2 ==0])     
'''
'''
li = ['a','b','c']
res = ""
for ch in li:
    res = res+ch+""
print(res)
print(" ".join(li))
''' 
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)