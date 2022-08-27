import math

T = int(input()) #테스트 데이터
# ==> for _ in range(int(input())): 으로 할수도 있음

for _ in range(T):
    H, W, N = map(int, input().split()) # 층수, 각층 방수, 몇번째손님
    
    if math.ceil(N/H)<=W:
        # 호수 구하기
        if math.ceil(N/H)<10:
            w = '0'+str(math.ceil(N/H))
        else:
            w = math.ceil(N/H)

        # 층수 구하기
        if N%H==0:
            h = H
        elif N>H:
            h = N%H
        else:
            h = N
    else:
        print('input error')
        break
    
    print('{}{}'.format(h,w))
    # ==> 앞에 0을 붙여 출력하고 싶으면 '0%d'로 작성해도 됨
