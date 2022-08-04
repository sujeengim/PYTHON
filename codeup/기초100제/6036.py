word, n = input().split()
print(word*int(n))
#다른 방법
for _ in range(int(n)):
    print(word, end='')