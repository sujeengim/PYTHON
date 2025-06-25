
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

