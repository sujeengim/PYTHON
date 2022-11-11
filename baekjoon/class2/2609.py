
n1, n2 = map(int, input().split())

#최대공약수 : 어떤수들의 공통 약수 중 가장 큰 수
#최소공배수 : 어떤수들의 공통 배수 중 가장 작은 수

lst = []
lst1 = []
lst2 = []

#최대공약수 구하기
for i in range(1,n1+1):
    for j in range(1, n1+1):
        if i*j == n1 and i not in lst1 and j not in lst1:
            lst1.append(i)
            lst1.append(j)
for i in range(1,n2+1):
    for j in range(1, n2+1):
        if i*j == n2 and i not in lst2 and j not in lst2:
            lst2.append(i)
            lst2.append(j)

lst = lst1+lst2
for i in lst:
    if lst.count(i)<2:
        lst.remove(i)
print(max(lst))

lst.clear()
lst1.clear()
lst2.clear()
#최대공약수 끝

#최소공배수 구하기
n=1
while True:
    lst1.append(n*n1)
    lst2.append(n*n2)
    lst = [i for i in lst1 if i in lst2]
    if len(lst)!=0:
        print(lst[0])
        break
    n+=1
#최대공배수 끝

#유클리드 호제법
import sys

A = sys.stdin.readline().split(" ")

A = list(map(int, A))

a = A[0]
b = A[1]

def gcd(a, b):
    sum = a%b
    if (a%b==0):
        return b
    else:
        return gcd(b, sum)

print(gcd(a, b))
print(a*b//gcd(a,b))