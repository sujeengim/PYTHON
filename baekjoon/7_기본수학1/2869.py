A, B, V = map(int, input().split())

go = 0
cnt=0

'''시간초과
100 99 1000000000 입력했을때
-> 반복문으로 풀지 마라'''
while go<V:
    cnt+=1
    if go+A >= V: # 정상에서는 B 적용 안됨
        break
    go+=(A-B)

print(cnt)

'''맞은 풀이'''
import math,sys
A, B, V = map(int, sys.stdin.readline().split())
print(math.ceil((V-A)/(A-B))+1)
#왜 (V-A)%(A-B)==0 일때도 +1을 해줘야 하는지 모르겠음