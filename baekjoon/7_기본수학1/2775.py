# 재귀로 해보기/


def fac(n_test):
    if n_test==0:
        return n_test
    else:
        return fac(n_test)

for _ in range(int(input())):
    k = int(input()) # 층
    n = int(input()) # 호

    if k==0:
        print(n)
        break
    if n==1:
        print(1)
        break

    ans = 0
    n_test = n
    num = 1
    while n_test>0:
        ans += num*n_test
        n_test-=1
        num+=1

    print(ans)