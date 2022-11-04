N = int(input())

bit = 0

for i in range(1,N):
    # 0. 생성자i 반복문(1~N)을 돌면서
    # 1. i의 자릿수(전체길이) 알아내기
    # 2. i+i의각자릿수를 더한값이 N과 같으면 i출력
    # 3. 생성자(i) 없으면 0출력
    s = i
    for a in str(i):
        s+=int(a)
    if s==N:
        print(i)
        bit = 1
        break
if bit == 0:
    print(0)