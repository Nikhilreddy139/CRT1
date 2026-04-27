a = [1,2,5,8,9,832,15,63]
print(max(a))
#check Palindrome(using reversed() and join())
s = input()
if s== "".join(reversed(s)):
    print("Palindrome")
else:
    print("Not a Palindrome")
#Count Even numbers using filter()
