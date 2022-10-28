#나이 오름, 가입일 오름

N = int(input())

a = []
n = []
s = []

for _ in range(N):
    age, name = input().split()
    age = int(age) #w정수형으로 따로 만들어주기
    s.append([age, name])

s.sort(key = lambda x: x[0])
#여러정렬기준 : key = lambda x : (x[0], x[1]) -> 우선 x[0]기준 정렬, 후 x[1]정렬

for i in s:
    print(i[0], i[1])