# Armstrong number
'''n = int(input())
l = len(str(n))
res = 0
for i in str(n):
    res +=int(i)**l
print("Armstrong"if n==res else "Not Armstrong")'''
#Perfect number
'''n = int(input())
s = 0
for i in range(1,n//2+1):
    if n%i==0:
        s +=i
print("Perfect" if n==s else "Not Perfect")'''
#Strong Number
def fact(n):
    if n<0:
        return "No factorial for _ve"
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact *=i
        return fact
s = 0
n = int(input())
for i in str(n):
    s +=fact(int(i))
print("Strong ")