N = int(input())

list = []

for _ in range(N):
    list.append(int(input()))

list.sort()

tp = tuple(list) #중복 제거

for i in tp:
    print(i)