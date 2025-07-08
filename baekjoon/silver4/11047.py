#11047
import sys

n, k = map(int, input().strip().split())
nlist = []  # 동전 종류
gap = k
cnt = 0

for i in range(n):
    na = int(sys.stdin.readline().strip())
    nlist.append(na)

'''
n: 동전의 종류 수
k: 동전의 총합 목표
gap : 남은 금액
cnt : 최소 사용된 동전 개수 
'''

nlist.sort(reverse=True)  

# gap 줄여가기 
'''
## 1. 시간초과
for i in range(len(nlist)):
    while gap > 0:
        if gap - nlist[i] >= 0:
            u = gap//nlist[i]
            gap -= nlist[i] * u
            cnt += u
        else:
            break
            
## 2. 논리오류
for i in range(len(nlist)):
    if gap - nlist[i] >= 0:
        cnt += gap//nlist[i]
        gap = gap%nlist[i]
    else:
        break
#-> gap이 현재 동전 (nlist[i])보다 작다면, 
# 다음으로 더 작은 동전들을 사용해서 남은 gap을 채워야 합니다. 
# 하지만 break가 실행되면 for 루프가 즉시 종료되어 버리고, 
# 뒤에 남아있는 더 작은 동전들은 아예 고려되지 않습니다.
'''

# 해결
for i in range(len(nlist)):
    if gap==0:
        break
    cnt += (gap//nlist[i])
    gap = gap%nlist[i]


print(cnt)
