n, m = map(int, input().split())

list1 = []
list2 = []

for a in range(n):
    list1.append(list(map(int, input().split())))

for a in range(n):
    list2.append(list(map(int, input().split())))

for a in range(n):
    for b in range(m):
        print(list1[a][b]+list2[a][b], end=' ')
    print()