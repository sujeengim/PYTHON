# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램


# 1. n이 10보다 작으면 0 두개 붙이기
# 2. n의 각 자리수 더한 값의 맨 오른쪽
# 3. n의 맨 오른쪽을 잇기
# 4. 만약 이은 값이 처음 값과 같다면 사이클 길이 반환
# 다시 1로
ori = int(input())
n_ori = int(ori) # 새로운 수 저장, 변수이름을 new같은걸로 지으면 보기에 좋을듯
length = 0
while True:
    if n_ori<10: # n_ori를 왜 str로 인식하는지 모르갰음
        n_ori=int('0'+str(n_ori)) #이건 왜 해줘야 하는걸까
        # print(n_ori)
    n2 = (n_ori%10)+(n_ori//10) #n_ori의 각 자리수 합
    n_ori = int(str(n_ori%10)+str(n2%10)) #여기서 int로 안바꿔줬음
    length += 1
    if n_ori==ori:
        print(length)
        break
