## 방법 1 _ 이게 왜 되는거지?
n = int(input())
soinsu = []

if n==1:
    print()
else:
    while n!=1:
        for k in range(2, n+1):
            if n%k == 0:
                soinsu.append(k)
                n = n//k
                break
for i in soinsu:
    print(i)

## 방법2
n = int(input())

def isprime(a):
    if a<2:
        return False
    for i in range(2,a):
        if a%i == 0:
            return False
    else:
        return True

for i in range(2,n+1):
    if n%i==0 and isprime(i):
        while n%i == 0:
            print(i)
            n = n//i
    else:
        pass