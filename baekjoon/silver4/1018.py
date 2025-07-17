# 약한 부분 1018
import sys
m, n = map(int, input().strip().split()) #열, 행

m_pot = 8-m
n_pot = 8-n
mnlist = []  

for _ in range(n): 
    row = list(sys.stdin.readline().strip())
    mnlist.append(row)
print(mnlist)

for i in range(n):
    for j in range(m_pot):
        temp = mnlist[i][j:j+8]
