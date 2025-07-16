# 10816 시간초과
'''
import sys

n = int(sys.stdin.readline().strip())
nlist = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
mlist = list(map(int, sys.stdin.readline().strip().split()))
cntlist = [0]*m
nlist.sort()

def bin_search(seq, target):
    pl, pr = 0, len(seq) - 1
    
    while True:
        pc = (pl+pr)//2
        if seq[pc] == target:
            return pc
        elif seq[pc] < target:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break

    return -1


for i in range(len(mlist)):
    while True:
        idx = bin_search(nlist, mlist[i])
        if idx == -1:
            # cntlist[i] = 0
            break
        cntlist[i]+=1
        nlist.remove(nlist[idx])
        bin_search(nlist, mlist[i])

print(*cntlist)  
'''

# 수정했는데 시간초과 => O(N log N + M * (log N + N))
'''
import sys

n = int(sys.stdin.readline().strip())
nlist = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
mlist = list(map(int, sys.stdin.readline().strip().split()))

nlist.sort() # O(nlogn)

def bin_search(seq, target): # O(logn)
    pl, pr = 0, len(seq) - 1
    
    while True:
        pc = (pl+pr)//2
        if seq[pc] == target: #있군
            return seq.count(target) #O(n)
            # return seq[pc:].count(target) # 논리오류
        elif seq[pc] < target:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr: #없군
            break

    return 0


for i in mlist:
    print(bin_search(nlist, i), end=' ')
'''

# 시간초과 해결 O(N+M)
import sys
from collections import Counter

n = int(sys.stdin.readline().strip())
nlist = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
mlist = list(map(int, sys.stdin.readline().strip().split()))

# nlist의 각 숫자의 개수를 미리 세어 딕셔너리로 저장
# 시간 복잡도: O(N)
n_counts = Counter(nlist)

results = []
for i in mlist:
    # 딕셔너리에서 바로 개수를 가져옴 (O(1))
    results.append(str(n_counts[i])) # 없으면 0 반환

print(' '.join(results))
