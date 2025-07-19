# 약한 부분 1018
'''
1. w와 b의 개수가 반반이 아니라면 그 차이만큼 count
2. wb가 교차하는지 하나씩 확인 
'''
import sys

m, n = map(int, input().strip().split()) #열, 행

m_pot = 8-m+1
n_pot = 8-n+1
mnlist = []  
min = 0

# m*n 체스판 만들기 
for _ in range(n): 
    row = list(sys.stdin.readline().strip())
    mnlist.append(row)
print(mnlist)

# 8*8 단위로 비교해서 최소 차이 구하기 
for i in range(n_pot):
    temp = mnlist[i:i+8]  #8행 선택
    for j in range(m_pot):
        temp2 = [inner_list[j:j+8] for inner_list in temp] #8열 선택
        cnt = 0
        for k in temp2: #선택된 8*8 단위의 행을 하나씩 확인
            cnt += k.count('W')  #W의 개수 세기
        if cnt >= 32:  #W가 더 많으면 B의 개수
            min = cnt - 32
        else:
            min = (64-cnt)-32

# print(temp2)

# testlist = [['안', '하', '반', '요', '무', '인', '음', 'W'],
#             ['냥', '세', '가', '이', '슨', '가', '겠', 'B'],
#             ['하', '야ㅕ', '워', '게', '일', '모', '르', 'W']]

# # 리스트 컴프리헨션
# result = [inner_list[1:3] for inner_list in testlist]
# print(result[0])  
