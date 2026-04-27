#Fibonacci Problem
'''def fibonacci(n):
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(10):
    print(fibonacci(i), end=" ")'''
#GCD of Two Numbers
def GCD(a,b):
    if b==0:
        return a
    return GCD(b , a % b)
#2
#def GCD(a,b):
 #   while b!=0:
        #a,b = b,a%b
    #return a
#print(GCD(48,6))
