m = 0
r, c = 1, 1

for i in range(1,10):
    t = list(map(int, input().split()))
    if max(t)>m:
        m = max(t)
        r = i
        c = t.index(max(t))+1

print(m)
print(r, c)