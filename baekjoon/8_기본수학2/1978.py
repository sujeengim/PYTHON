n = int(input())

nlist = list(map(int, input().split()))
ans =0

for a in nlist:
    count=0
    for x in range(1,101):
        if x==a:
            break
        if a/x==a//x: #나누어 떨어지면 카운트
            count+=1
    if count==1:
        ans+=1

print(ans)