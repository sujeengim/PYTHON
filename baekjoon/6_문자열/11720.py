N=int(input())
number=input()
sigma=0
for i in range(N):
    sigma+=int(number[i])
print(sigma)

# 반복문 사용 x but n개 제한 불가
n = input()
print(sum(map(int, input()))) #map도 sum 사용 가능하군.