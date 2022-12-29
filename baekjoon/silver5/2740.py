# 행렬곱셈 조건 : 첫째 행렬 열 개수 == 둘째 행렬 행 개수 

import sys

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
m, k = map(int, sys.stdin.readline().split())
b = [list(map(int, sys.stdin.readline().split())) for i in range(m)]

ans = [[]*n]
print('ans : ',ans)

for i in range(n): #a행만큼, a의 행 차례로 선택
    x = []
    for j in range(k): #b열만큼, b의 열 차례로 선택
        s = 0
        for k in range(m): #b행만큼, a행 요소 차례로 선택
            s += a[i][k]*b[k][j]
        x.append(s)
    ans.append(x)