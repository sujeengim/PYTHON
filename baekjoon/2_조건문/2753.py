# 연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램

y = int(input())
if (y%4==0 and y%100!=0) or y%400==0:
    print("1")
else:
    print("0")