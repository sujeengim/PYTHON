import sys
N, X= map(int, input().split())
a = sys.stdin.readline().rstrip().split()
for i in range(0,N):
    if int(a[i])<X:
        print(a[i], end=' ')

#처음 시도 문제 : N개를 넘는 입력을 받아도 반영된다.
for i in a:
    if int(i)<X:
        print(i, end='')