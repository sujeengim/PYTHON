# 행렬곱셈 조건 : 첫째 행렬 열 개수 == 둘째 행렬 행 개수 

import sys

n, m = map(int, sys.stdin.readline())
a = [list(map(int, sys.stdin.readline())) for i in range(n)]
m, k = map(int, sys.stdin.readline())
b = [list(map(int, sys.stdin.readline())) for i in range(m)]

