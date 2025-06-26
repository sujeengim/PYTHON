
def primeNumber(n):
  '''소수 구하기'''
    primeList = [2]
    
    for check in range(3, n+1, 2):
        checkPrime = 0
        for prime in primeList:
            if check % prime == 0:
                checkPrime = 1
                break
        if checkPrime:
            continue
        else:
            primeList.append(check)
            
    return primeList


def partition(n:int):
  '''골드바흐 파티션 개수 구하기'''
    cnt = 0

    primeList = primeNumber(n)

    return cnt


def main():
    n = int(input())
    numList = [0]*n
    cntList = [0]*n

    for i in range(n):
        numList[i] = int(input())

    for i in numList:
        cntList[i] = partition(n)

    for cnt in cntList:
        print(cnt)

if __name__ == "__main__":
    main()
