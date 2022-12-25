import math

'''
m개 중 n개 취해 조합 : mCn = m! / (n!(m-n)!)
'''

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    ans = math.factorial(m) // (math.factorial(n)*math.factorial(m-n))
    print(ans)