n, k = map(int, input().split())

# n! / (n-k)!*k!

def fac(a):
    if a==0:
        return 1
    ans = 0
    for i in range(a+1, 1, -1):
        ans *= i
    return ans

print(fac(n) / (fac(n-k)*fac(k)))