#메모리 초과 코드
#append는 메모리 재할당이 이루어져 메모리 많이 사용 

n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))

lst = sorted(lst)

for a in lst:
    print(a)


# 수정
import sys

n = int(input())
lst = [0] * 10001

for a in range(n):
    lst[int(sys.stdin.readline())] += 1

for a in range(len(lst)):
    if lst[a] != 0:
        for _ in range(lst[a]):
            print(a)