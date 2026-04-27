'''
1.Linear Search(sequential)
2.Binary Search(Interval)
'''
'''def Linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
li = list(map(int,input().split()))
target = int(input())
print(Linear_search(li,target))
target1 = int(input())
print(Linear_search(li,target1))'''
def Binary_search(arr, target):
    arr.sort()  
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(Binary_search([2,5,7,8,10,20,336,45], 7))  # 2