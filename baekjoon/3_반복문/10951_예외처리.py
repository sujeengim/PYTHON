# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except ValueError:
        break