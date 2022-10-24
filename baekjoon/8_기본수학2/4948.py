import math

def prime(p):
    prime_list = []
    for i in range(p, 2*p+1):
        im = 0
        for j in range(2, int(math.sqrt(i))+1):
            if i%j==0:
                im = 1
                break
        if im == 0 and i != p:
            prime_list.append(i)
    return prime_list

while True:
    n = int(input())

    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        prime_cnt = len(prime(n))

        print(prime_cnt)