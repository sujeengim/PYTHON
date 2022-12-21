import sys

n = int(input())

lst = ['*', ' '] * 51

for _ in range(n):
    s = ''
    for i in lst[:n]:
        s += i
    print(s)
    s = ''
    for i in lst[1:n+1]:
        s += i
    print(s)
sys.exit('Finish ^.^')

'''
## 다른 풀이1

for i in range(n):
    print('* '*((n+1)//2))
    print(' *'*((n)//2))

## 다른 풀이2

if n==1: print('*'); quit() # 코드 중단 

s = '* '*n
for _ in range(n):
    print(s[:0].rstrip()); print(s[n:][::-1].rstrip()) #문자열 오른쪽 공백 제거
'''