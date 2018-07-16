def palindrome(n):
    if n ==  n[::-1]:
        return True
    return False

res = []
for i in range(1,1000000):
    s = str(i)
    if palindrome(s):
        s= bin(i)
        if palindrome(s[2:]):
            res.append(i)

print(res)
print(sum(res))