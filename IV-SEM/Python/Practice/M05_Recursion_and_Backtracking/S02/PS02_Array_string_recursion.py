#Find sum of array elements
'''def Array_sum(nums):
    s=0
    for i in range(len(nums)):
        s+=nums[i]
    return s
print(Array_sum([10,20,30,40]))
def Array_sum_recursion(nums,i):
    if i==-1:
        return 0
    return nums[i]+Array_sum_recursion(nums,i-1)
print(Array_sum_recursion([10,20,30,40],3))
def Array_sum_recursion(nums):
    if len(nums)==0:
        return 0
    return nums[-1]+Array_sum_recursion(nums[:-1])
print(Array_sum_recursion([10,20,30,40]))
#Reverse Array elements using recursion
def Reverse_Array(nums,i,j):
    if i>=j:
        return nums
    nums[i],nums[j]=nums[j],nums[i]
    return Reverse_Array(nums,i+1,j-1)
print(Reverse_Array([1,2,3,4,5],0,4))
#Reverse a String using Recursion
def Reverse_String(st):
    if st=="":
        return ""
    return st[-1]+Reverse_String(st[:-1])
print(Reverse_String("a,b,c"))
#Palindrome
def is_palindrome(st):
    return st==Reverse_string(st)
print(is_palindrome("abc"))
print(is_palindrome("mam"))'''
#Digital root
def Digital_root(n):
    if n<=9:
        return n
    s = sum([int(i) for i in str(n)])
    return Digital_root(s)
print(Digital_root(456))
