from typing import Set
# 1~100 사이 소수
def primeNumber(n:int)->Set[int]:
    primeSet = {2}

    for check in range(3, n+1, 2):# 1.짝수 건너뛰기
        checkPrime = 0
        for prime in primeSet:
            if check % prime == 0: # 2.소수로 나누어떨어지면
                checkPrime = 1
                break
        if checkPrime:
            continue
        else:
            primeSet.add(check) # 3.추가

    print(primeSet)

    return primeSet


def partition(n:int)->int:
    cnt = 0

    primeSet = primeNumber(n)
    roopSet = primeSet.copy()
    # print(primeSet)

    #주의: 중복제거
    print("반복문 시작") 
    for p1 in primeSet:
        #주의: 인덱스 설정 (primelist에서만 가져오기)
        for p2 in roopSet: #p1~나머지set
            print(p1,p2)
            p = p1+p2
            if p == n:
                cnt += 1
            elif p > n:
                break
        roopSet.remove(p1)

    return cnt


def main():
    n = int(input())
    numList = [0]*n
    cntList = [0]*n

    for i in range(n):
        numList[i] = int(input())

    # print("print numberList: ",numList)

    #주의: 인덱스 설정
    for i in range(len(numList)):
        # print("지금 무슨 숫자가 가는가?@",numList[i])
        cntList[i] = partition(numList[i])

    for cnt in cntList:
        print(cnt)

if __name__ == "__main__":
    main()
