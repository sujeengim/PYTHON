# 점의 좌표를 입력받아 그 점이 어느 사분면에 속하는지 알아내는 프로그램

x, y = map(int, [input() for _ in range(2)])
if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
else:
    print("4")