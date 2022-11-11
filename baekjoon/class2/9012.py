# ( -> +1
# ) -> -1
# 마지막에 합 0이 아니면 vps가 아님
# ==>이렇게 하면 괄호 개수는 맞지만 방향이 맞지 않음

'''
두 리스트를 만들어서 하나씩 비교하며 
짝이 되는지 확인
'''

n = int(input())

for i in range(n):
    ss = input()
    c = 0

    for s in ss:
        if s=='(':
            c+=1
        elif s==')':
            c-=1
        if c<0: #열리지도 않았는데 닫은 경우!!
            print('NO')
            break
    if c>0:
        print('NO')
    elif c==0:
        print('YES')