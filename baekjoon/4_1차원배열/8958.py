# n = int(input())
# test=[]
# for _ in range(n):
#     # test = sys.stdin.readline().rstrip().split('\n') #맨 마지막 값만 리스트로 저장됨.
#     test.append(input())
# for i in test:
#     score = 0 # 점수 저장
#     count = 0 # test의 요소마다 점수 저장
#     for j in range(len(i)):
#         if i[j]!='X':
#             count+=1
#             score+=count
#         else:  
#             count=0
#     print(score)
# print(test)

# sys.stdin.readline() 사용 & 입력 값 저장해둘 필요 없음
import sys
for _ in range(int(sys.stdin.readline())):
    score = 0  
    sum_score = 0
    for ox in list(sys.stdin.readline()):
        if ox == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)