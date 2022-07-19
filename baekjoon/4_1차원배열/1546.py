import sys

N = int(input())
score = list(map(int, sys.stdin.readline().rstrip().split()))
# score=sys.stdin.readline().rstrip().split() #리스트로 저장됨.
# score = list(map(int, input().split())
M = max(score)
for i in range(N):
    score[i] = score[i]/M*100
print(sum(score)/N)