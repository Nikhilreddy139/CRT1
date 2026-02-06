#1.Write a python code to count the digits of number?
'''a = int(input())
b = len(str(a))
print(b)'''
#2.sum of digits of given number
'''num = int(input())
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
print(sum)'''
#3.Product of digits of given number
'''num = int(input())
sum = 1
while num > 0:
    sum *= num % 10
    num //= 10
print(sum)'''
#4.Reverse a given number
'''num = input()
print(num[::-1])'''
#5.Count the even and odd digits in given number
'''num = int(input())
even = 0
odd = 0
while(num>0):
    d = num%10
    if(d%2==0):
        even +=1
    else:
        odd+=1
    num //=10
print("Even count",even)
print("Odd count",odd)'''
#6.Largest digit of given number
num = int(input())
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10
print(largest)


