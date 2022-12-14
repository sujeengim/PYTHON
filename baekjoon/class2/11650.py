n = int(input())

lst = []

for i in range(n):
    lst.append(tuple(map(int, input().split())))

lst = sorted(lst)

for i in lst:
    print(i[0], i[1])