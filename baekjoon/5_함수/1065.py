N=int(input())
if N>=100:
    n = 99
    for i in range(100,N+1):
        c = i%10 #한수 판별 시작할 가장 오른쪽 자리 수
        c2 = i//10 #c뺀 나머지 수
        d = (c)-(c2%10) #연속된 두 수 차이
        while True:
            if (c+d) == (c2%10):
                c2=c2//10
            else:
                break
            if c2<=0:
                n+=1
                break
else:
    n = N
print(n)