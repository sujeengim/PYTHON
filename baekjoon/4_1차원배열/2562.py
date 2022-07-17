# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램
import sys
num = []
for _ in range(9):
    num.append(int(sys.stdin.readline().rstrip()))
print(max(num), num.index(max(num))+1, sep='\n')