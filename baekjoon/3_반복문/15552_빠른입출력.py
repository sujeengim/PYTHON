# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
# input의 경우, 반복적으로 입력되는 양이 많을 경우 입력 시간이 길어진다.
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# 하지만 sys.stdin.readline은 한줄단위로 입력을 받아, 마지막에 개행 문자가 포함된다. 
# 개행문자를 없애려면 rstrip 사용. 공백을 없애려면 strip


import sys

T = int(sys.stdin.readline()) #여기서는 그냥 input으로 해도 상관없을까?
for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


# 아래처럼 함수를 변수에 할당하여 간단한 이름으로 활용 가능
# input_readline = sys.stdin.readline
# a, b = map(int, input_readline().split())