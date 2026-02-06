import numpy as np
'''arr = np.array([10,20,30])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers list is:",np.arange(2,10,2))
print("Odd numbers list is:",np.arange(1,10,2))
n = int(input("Enter the size"))
ele = list(map(int,input().split()))
print("Array Ele are:",np.array(ele))
# 3rd distinct max Number
nums = list(map(int, input().split()))
if len(nums) >= 3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))'''

# Monotonic number
nums = list(map(int, input().split()))
inc = True
dec = True
for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        inc = False
    if nums[i] > nums[i - 1]:
        dec = False
print(inc or dec)


