#Count of factors of a given number
'''n = int(input())
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i)
print("Count of factors:", count)'''
# Reversing a number with signs and zero
'''n = int(input())

if n >= 0:
    print(int(str(n)[::-1]))
else:
    n = -1*n
    print(-1*int(str(n)[::-1]))'''
# Even or Odd
n = int(input())
if n <= 1:
    print("Not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n,"Is Not a Prime")
            break
    else:
        print(n,"Is a Prime")

