#런타임에러
n, m = map(int, input().split())

lst = list(map(int, input().split()))

def fac(x):
    ans = 1
    for _ in range(1,x+1):
        ans *= x
        x -= 1
    return ans

s = [0] * fac(n)


index = 0

for a in lst:
    for b in lst:
        if (a==b) or (a+b > m):
            continue
        for c in lst:
            if (a==c) or (b==c) or (a+b+c > m):
                continue
            s[index] = a+b+c
            index += 1

print(max(s))