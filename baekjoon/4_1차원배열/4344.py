import sys
C = int(input())
result = [] # 각 케이스의 평균 넘는 비율 저장
for _ in range(C): # 케이스 반복(행 반복)
    
    s = 0 # 각 케이스의 점수들 저장
    count = 0 # 각 케이스의 평균보다 높은 점수 세기
    score = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(score)): # 각 케이스 반복(열 반복)
        s +=score[i]
    for i in range(1, len(score)):
        if score[i] > s/score[0]:
            count+=1
    result.append(format(count/score[0]*100, ".3f"))
for i in result:
    print(i,"%",sep='')