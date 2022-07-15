# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램

# 두번째 방법
import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().rstrip().split())) #list로 만들어야함. 바꾸지 않으면 list가 아닌 map객체임.
print(min(arr), max(arr))

#첫번째 방법
N = int(input())
list = [int(x) for x in input().split()]
min = list[0]
max = list[0]
for i in range(N):
    if min>list[i]:
        min = list[i]
    if max<list[i]:
        max = list[i]
print(min, max)