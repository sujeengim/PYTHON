# [기초-입출력] 시간 입력받아 그대로 출력하기
# 24시간 시:분 형식으로 시간이 입력될 때, 그대로 출력하는 연습을 해보자.

#sep : seperator
#처음 풀이
# x = input() 
#->여기서 12:12 이렇게 입력하면 그대로 저장
# print(x) 
#-> 출력

# 또 같은 실수. map을 기억하자
# h, m = int(input().split(':'))
h, m = map(int, input().split(':'))
if 0<=h<60 and 0<=m<60:
    print(h, m, sep=':')
else:
    print("제대로 입력하세요")  