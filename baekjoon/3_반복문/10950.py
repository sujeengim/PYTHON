# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램

n = int(input())
answer = []
for i in range(n):
    A, B = map(int, input().split())
    answer.append(A+B)
for i in range(n):
    print(answer[i])
