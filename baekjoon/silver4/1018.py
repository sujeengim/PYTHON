# 약한 부분 1018
import sys

m, n = map(int, input().strip().split()) #열, 행

m_pot = 8-m+1
n_pot = 8-n+1
mnlist = []  
min = 0

# m*n 체스판 만들기 
for _ in range(n): 
    row = list(sys.stdin.readline().strip())
    mnlist.append(row)
print(mnlist)

# 8*8 단위로 비교해서 최소 차이 구하기 
for i in range(n_pot):
    temp = mnlist[i:i+8]  
    for j in range(m_pot):
        temp2 = [inner_list[] for inner_list in temp]
