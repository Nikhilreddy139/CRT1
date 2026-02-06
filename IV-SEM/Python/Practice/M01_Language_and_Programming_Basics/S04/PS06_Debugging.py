'''Debugging in python
bug --> Errors
debugging --> process of finding and fixing of errors
Types of errors:
    1.Syntax errors:
        Missing of colons and indentation
    2.Runtime errors:
        Division by Zero
    3.Logical errors:
        Missing of logics
Debugging Techniques:
    1.print()
    2.try-except
    3.Using pdb
3.pdb-->Python Debugger
purpose:
    1.pause the execution code
    2.insert the variables value
    3.to run the code line by line
    pdb commands:
    1.n-->to execute the output in next line
    2.p variable -->to get the value of a variable
    3.l --> List nearby code
    4.c --> continue the execution
    5.s --> To start a function
    6.r --> To return from the function
    7.h --> To help
    8.q --> Quick the execution 


try:
    a = int(input())
    print(10/a)
except ZeroDivisionError:
    print("Can not divisible by Zero")
except ValueError:
    print("Invalid input")
'''
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a = int(input())
b = int(input())
print(add(a,b))