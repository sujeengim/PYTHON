t = int(input())

dp = [[0]*15 for _ in range(15)] # 15*15
dp[0] = [x for x in range(15)] #0층은 각 호만큼 사람이 채워짐

'''sol 1'''
for i in range(1, 15): #층 만들기
    for j in range(1, 15): #호 만들기
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # i층j호는 자신의 앞 호 숫자에 자신 아래층 같은호 숫자를 더한것과 같다
'''sol 1 end'''


'''sol 2 => 느림'''
for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j+1):
            dp[i][j] += dp[i-1][k]
            # i층j호는 자신 아래층에서 j호까지 숫자를 더한것과 같다
            '''
            eg)
            dp[1][1] = dp[0][1] + dp[0][2] 
            dp[1][2] = dp[0][1] + dp[0][2] + dp[0][3]
            .
            .
            .
            dp[3][1] = dp[2][1] + dp[2][2]
            dp[3][2] = dp[2][1] + dp[2][2] + dp[2][3]
            .
            .
            .
            '''
'''sol 2 end'''


for _ in range(t):
    k, n = int(input()), int(input())
    print(dp[k][n])