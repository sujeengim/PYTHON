import sys

n, k = map(int, input().strip().split())
nlist = []
gaplist = []

for _ in range(n):
    nlist.append(sys.stdin.readline().strip())
    gaplist.append(abs(k - int(nlist[-1])))

gaplist.sort() 

for i in range(n):
    if gaplist[i] == 0:
        print(n+1)
