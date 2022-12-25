import math

'''
m개 중 n개 취해 조합 : mCn = m! / n!(m-n)!
'''

t = int(input())
# n개 정하기
# for _ in range(t):
#     n, m = map(int, input().split())

    # ans = math.factorial(m) // math.factorial(n)*math.factorial(m-n)
    # print(ans)

c = 1
ans = 0 
for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n):
        # ans += math.factorial(m-c) // math.factorial(c)*math.factorial(m-c)
        ans += (m-c)
        c += 1
    print(ans)
