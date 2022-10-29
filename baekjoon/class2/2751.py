# 시간초과
N = int(input())

list = []

for _ in range(N):
    list.append(int(input()))

list.sort()

tp = tuple(list) #중복 제거

for i in tp:
    print(i)

# pypy로 풀기
N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))

arr.sort()
for i in arr:
    print(i)