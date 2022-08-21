# 한 라인 최대숫자 1, 7, 19, 37, 61
# 한 라인 칸 수 1, 6, 12, 18, 24, 30
# 규칙 찾기     1, 6*2-6, 6*3-6, 6*4-6, 6*5-6, 6*6-6, ...
# 다음 라인에 추가되는 칸 수 +1, +5, +6, +6, +6, 

# 시간초과 풀이방법
'''시간초과 이유 : N은 10억까지 가능한데 그걸 언제 for문을 하고 있어'''
N=int(input())
cnt=1
ans=1
for i in range(N):
    cnt+=1
    if cnt==ans*6:
        cnt=0
        ans+=1
    if i==N-1 and cnt!=0:
        ans+=1
print(ans)

# 틀린 풀이
'''틀린이유 : 아직 모름'''
N=int(input())-1 #2부터 시작
ans=1 #방을 지나는 횟수 (처음과 끝이 포함. 처음을 미리 추가해둠)
cnt=0 #한 라인을 넘어갈때마다 1추가
while N>6:
    '''
    라인이 증가하면 원래 라인의 벌집 개수+6이 된다
    2부터 N까지 6, 6*2(cnt), 6*3(cnt)씩 N에서 제거할때마다 ans를 1증가한다
    N이 6보다 작아질때까지 반복한다
    N에서 6*cnt를 제거한 값이 0보다 작으면 반복을 멈춘다.
    '''
    cnt+=1
    if N-(6*cnt)<0:
        break
    N=N-(6*cnt) 
    ans+=1
ans+=1
print(ans)

# 틀린 풀이2
'''N이 58일때 11이 나왔다.
now는 현재 숫자를 저장하고 있어야 하는데
이건 now에 현재 라인의 최대 칸수를 저장한다.'''
N = int(input())
cnt = 0
while True:
    cnt += 1
    now = (cnt*6-6)
    if now >= N:
        break   
    else:
        pass
print(cnt)

# 해결
N = int(input())
cnt = 0
now = 1 # 1부터 시작
while True:
    cnt += 1
    now += (cnt*6-6) # 누적으로 수정
    if now >= N:
        break   
    else:
        pass
print(cnt)