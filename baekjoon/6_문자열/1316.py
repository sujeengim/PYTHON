import sys

n = int(input())
count=0
for i in range(n):
    w = sys.stdin.readline()
    lst = [w[0]] #미리 첫번째요소 담아두기
    for i in range(1,len(w)): #첨엔 (1,len(w)+1)이라고 했었는데 마지막요소까지만 하는게 맞죠
        '''
        처음 등장하는 문자는 리스트에 넣고
        리스트에 있는데 앞문자와 현재문자가 같은 값이면 pass
        리스트에 있는데 앞문자와 같지 않은 문자는 카운트
        '''
        if w[i] in lst and w[i]!=w[i-1]: #두번째요소부터 마지막요소까지 자기앞요소로 검사
            count+=1
            break
        elif w[i] not in lst:
            lst.append(w[i])
print(n-count)