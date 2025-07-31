import sys

n = int(input())
cnt0 =0
cnt1 =0
for i in range(n):
    f = int(sys.stdin.readline().strip())
    if f == 0:
        cnt0 += 1
    elif f == 1:
        cnt1 += 1
