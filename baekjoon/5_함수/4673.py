# 함수
def selfnumber(n):
    '''n보다 작거나 같은 셀프 넘버 출력'''
    creation = [] # 생성자 저장 리스트
    selfnum = [] # 셀프 넘버 저장 리스트
    for i in range(1, n+1):
        plus = i
        while True:
            if i<=0: # 쓸데없는 조건 확인은 하지 말자. false는 0이다.
                break
            plus += (i%10)
            i //= 10
        creation.append(plus)
    for i in range(1,n+1):
        if i not in creation:
            selfnum.append(i)
    return selfnum

selfnumber(10000)

# 함수 사용 x
creation = [] # 생성자 저장 리스트
for i in range(1, 10001):
    plus = i
    while True:
        if i<=0:
            break
        plus += (i%10)
        i //= 10
    creation.append(plus)
for i in range(1,10001):
    if i not in creation:
        print(i)