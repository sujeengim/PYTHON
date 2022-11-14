n = input().split()
print(n)
s = 0

for i in n:
    s += (int(i))**2
print(s)
print(s%10)
