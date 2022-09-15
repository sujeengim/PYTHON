m = int(input())
n = int(input())

list = []
what = 1 #이거 왜 있어야 돼??????????????????????????????????

for x in range(m,n+1):
    if x>1: #이거 없으면 m이 1일때 소수에 1포함됨
        for i in range(2,x):
            if x%i==0:
                what=0
                break
            else:
                what=1
        if what==1:
            list.append(x)

# if len(list)==0:
if list == []:
    print(-1)
else:
    print(sum(list), min(list), sep='\n')