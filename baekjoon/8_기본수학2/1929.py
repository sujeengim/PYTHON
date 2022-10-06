import math

m, n = map(int, input().split())
r_n = int(math.sqrt(n))

def isprime(a):
    if a == 1:
        return False
    # 2~a까지 검사하지 말고 a의 제곱근까지만 검사하면 판단가능
    for i in range(2, int(math.sqrt(a))+1):
        if a%i==0:
            return False
    return True

for i in range(m,n+1):
    if isprime(i):
        print(i)