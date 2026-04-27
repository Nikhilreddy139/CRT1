# Sum of n natural numbers
'''def sum_natural_numbers(n):
    if n < 0:
        return "Enter a positive integer"
    else:
        return n * (n + 1) // 2
print(sum_natural_numbers(10))'''
#Factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif(n<-1):
        print("Enter a Positive integer")
    else:
        return n * factorial(n - 1)
print(factorial(5))
