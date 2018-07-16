import math

def is_pandigital(n):
    n=list(str(n))
    n.sort()
    n="".join(n)
    number ='123456789'
    number=number[:len(n)]
    if n == number:
        return True
    return False

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


n = 7654321

while True:
    if is_pandigital(n) and is_prime(n):
        break
    n-= 2

print(n)

