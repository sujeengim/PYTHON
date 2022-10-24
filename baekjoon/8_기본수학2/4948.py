## 시간초과
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

## 답
import sys

#소수 찾기
def decimal(x):
    if x == 1:
        return False
    for k in range(2, int(x**0.5)+1):
        if x % k == 0:
            return False
    return True

#가능한 모든 수가 소수인지 확인
decimal_nums = []
for i in range(2, 246912):
    if decimal(i):
        decimal_nums.append(i)

#반복문을 통해 케이스를 확인
while True:
    n = int(sys.stdin.readline())
    cnt = 0

    #입력 받은 수가 0이면 반복을 멈춤
    if n == 0:
        break

    #소수인 수를 반복하여 구간에 있는지 확인
    for j in decimal_nums:
        #구간에 있으면 카운트
        if n < j <= 2*n:
            cnt+=1
    print(cnt)