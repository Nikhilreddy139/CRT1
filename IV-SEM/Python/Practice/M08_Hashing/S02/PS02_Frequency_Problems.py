#Count freq of elements(using dict and using counter)
#Using Dict
'''arr = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
print(freq)
#Using Counter
from collections import Counter

arr = [1, 2, 2, 3, 3, 3, 4]

freq = Counter(arr)

print(freq)
#2.
a=[1,2,1,2,1,4,2,5]
print(len(set(a)))
#3.Find Element with max Frequency
arr = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for x in arr:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1
max_elem = max(freq, key=freq.get)
print("Element:", max_elem)
print("Frequency:", freq[max_elem])'''
#4.First non-repeating element
a = [1,2,1,2,1,4,2,5]
freq = {}
for x in a:
    freq[x]=freq.get(x,0)+1
for x in a:
    if freq[x]==1:
        print(x)
        break