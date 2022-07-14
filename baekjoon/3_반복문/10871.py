import sys
N, X= map(int, input().split())
arr = []
for i in range(N):
    arr.append(sys.stdin.readline().rstrip().split())
    if i<X:
        arr.pop(i)
print(' '.join(arr))