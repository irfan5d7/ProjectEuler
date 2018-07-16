from math import factorial

f = [factorial(0),
factorial(1),
factorial(2),
factorial(3),
factorial(4),
factorial(5),
factorial(6),
factorial(7),
factorial(8),
factorial(9)]

res=[]
def fac_digits(n):
    sum = 0
    while n:
        sum+=f[n%10]
        n//=10
    return sum

for i in range(10,100000):
    if fac_digits(i) == i:
        res.append(i)
print(res)
print(sum(res))