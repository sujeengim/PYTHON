# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
import sys
T = int(input())
for i in range(1, T+1):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #{}: {}".format(i, a+b))