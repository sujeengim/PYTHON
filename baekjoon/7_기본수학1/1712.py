# 손익분기점 : 총 수입이 총 비용보다 많아지는 지점
'''
a = 고정비용
b = 노트북 한 대 생산비
c = 노브북 한 대 가격
'''

a, b, c = map(int, input().split())

# c*x = a*(b*x) -> x = a/(c-b)
if b>=c:
    print(-1)
else:
    print(a//(c-b)+1) 

# 처음 풀이 --> 손익분기점이 존재하지 않을때 -1 출력 못함
x = 1
while a*(b*x)<(c*x):
    x+=1
print(x)