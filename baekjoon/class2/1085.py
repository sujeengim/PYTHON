import math

x, y, w, h = map(int, input().split())

'''
직사각형 (0,0)~(w,h)
한수 (x,y)

안에 위치할 경우 :
점 사방면의 거리를 체크하여 가장 짧은 위치 출력

밖에 위치할 경우 :
    case1:
    x>w and y<=h
    case2:
    x<=w and y>h
    case3:
    x>w and y>h
'''

if x<=w and y<=h:
    check = []
    check.append(w-x)
    check.append(x)
    check.append(h-y)
    check.append(y)

    print(min(check))

else:
    if x>w and y<=h:
        print(x-w)
    elif x<=w and y>h:
        print(y-h)
    else:
        print(math.sqrt(x^2 + y^2))