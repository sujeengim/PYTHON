# 드디어 왔다 설탕문제...

n = int(input())
ans = 0

if (n%5)%3 == 0: # 3과5킬로그램이 모두 필요한 경우
    '''
    n이 11일때 5*1 + 3*2로 가능함.
    n
    '''
    test1 = n//5
    test1 += (n%5)//3

elif n%5==0: #5킬로그램만 필요
    ans += n//5
elif n%3==0: #3킬로그램만 필요
    ans += n//3
else:
    ans = -1
print(ans)