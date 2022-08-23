# 벌집과 비슷한 것 같다

# 1, 2, 3, 4, 5, 6
# 대각선 마다 갖는 칸 수 1, 3, 6, 10, 15, 21
# 대각선 마다 갖는 칸 수의 등차 +1, +2, +3, +4, +5, ...

'''틀린 풀이 ->3 넣으면 안됨.
같은 대각선 라인의 분모는 같다고 착각함'''
X = int(input()) #번째가 주어짐
cnt=1 #반복 횟수 저장. 대각선 한줄을 채울때마다 1증가
now=1 #번째 저장. 채워진 칸 하나하나의 개수 저장
if X==1:
    print('1/1')
else:
    while True:
        cnt+=1
        now+=cnt
        if X<=now:
            now-=cnt
            for i in range(1,cnt+1):
                now+=1
                if X==now:
                    now=i
                    break
            break
    print('{}/{}'.format(now,cnt))

'''틀린 풀이2 ->4 넣으면 안됨
배열을 이동하는 지그재그를 이해하지 못함'''
# 가로, 세로를 따로 접근해야겠음

X = int(input())
now=1 #첫번째 행의 분모만큼 생성&누적. 분자
col=1 #첫번째 행의 열 증가. 분모

if X==1:
    print('1/1')
else:
    while True:
        col+=1
        now+=col
        if X<=now:
            now-=col
            for i in range(1,col+1):
                now+=1
                if X==now:
                    now=i
                    col=col-(i-1)
                    break
            break
    print('{}/{}'.format(now,col))


''''''
X = int(input())
now=1 #대각선 개수만큼 현재 대각선에 칸 생성&누적
col=1 #대각선 개수 저장
cnt=1 #대각선 개수 증가하다가 72번째 줄에서 분수로 만들기 위한 준비를 함
if X==1:
    print('1/1')
else:
    while True:
        cnt+=1 # 대각선 증가
        now+=cnt # 현재 대각선에서 가질 수 있는 가장 큰 수 저장
        if X<=now:
            col=cnt #대각선 개수 col에 옮겨두기
            now-=col #현재 대각선 중 어디에 있는지 찾기 위해
            for i in range(1,col+1):
                now+=1
                if X==now:
                    now=i
                    cnt=cnt-(i-1)
                    break
            break
    # col -> 현재 대각선 개수를 분모에 or 분자에 적을것인지 결정
    if col%2==0:
        print('{}/{}'.format(now,cnt))
    else:
        print('{}/{}'.format(cnt,now))