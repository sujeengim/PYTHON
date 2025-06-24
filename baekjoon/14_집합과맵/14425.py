n, m = map(int, input().strip().split(' '))
cnt = 0

nlist = [0] * n 
mlist = [0] * m

for i in range(n):
    nlist[i] = input()

for i in range(m):
    mlist[i] = input()

for word in mlist:
    if word in nlist:
        cnt+=1

print(cnt)
