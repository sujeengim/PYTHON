# (몸무게, 키)
# 더 큰 덩치의 사람의 수

n = int(input())

wh = []
rank = [1 for i in range(n)]

for _ in range(n):
    x, y = map(int, input().split())

    wh.append((x, y)) 
    #튜플로 저장하고 싶을때 tuple()이 아니라 걍 괄호로 묶기

for i in range(n):
    #튜플은 값을 변화시킬 수 없다는 것만 제외하면 리스트와 동일
    for j in wh:
        if wh[i]!=j:
            if wh[i][0] < j[0] and wh[i][1] < j[1]:
                rank[i]+=1
                
            # elif wh[i][0] == j[0] and wh[i][1] < j[1]:
            #     rank[i]+=1
            # elif wh[i][0] < j[0] and wh[i][1] == j[1]:
            #     rank[i]+=1
for i in rank:
    print(i, end=' ')