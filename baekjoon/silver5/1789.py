import sys

s = int(sys.stdin.readline())

p, cnt = 0,0
for i in range(1,s+1):
    p += i #1부터 계속더해
    cnt += 1

    if p+(i+1)<=s:
        pass
    else:
        break
print(cnt)