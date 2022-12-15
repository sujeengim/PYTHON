emt = list()

for i in range(3):
    emt.append(tuple(map(int, input().split())))

def dot(x1, x2, y1, y2):
    return (x1*x2 + y1*y2)

# if ((emt[0][1]-emt[1][1])/(emt[0][0]-emt[1][0])) == ((emt[0][1]-emt[2][1])/(emt[0][0]-emt[2][0])): ==> 분모가 0이 될수도 있음
if ((emt[0][1]-emt[1][1])*(emt[0][0]-emt[2][0])) == ((emt[0][1]-emt[2][1])*(emt[0][0]-emt[1][0])):
    print('X')
else:
    a = ((emt[0][0]-emt[1][0])**2 + (emt[0][1]-emt[1][1])**2)
    b = ((emt[0][0]-emt[2][0])**2 + (emt[0][1]-emt[2][1])**2)
    c = ((emt[1][0]-emt[2][0])**2 + (emt[1][1]-emt[2][1])**2)
    leng = [a,b,c]
    # print('삼각형 길이^2 : ',leng)
    long = max(leng)
    # print('가장 긴 길이 : ', long)

    if a==b==c:
        print('JungTriangle')
    elif a==b or b==c or c==a:
        leng.remove(long)

        if (
            dot(emt[0][0]-emt[1][0], emt[0][1]-emt[1][1], emt[2][0]-emt[0][0], emt[2][1]-emt[0][1]) < 0 or
            dot(emt[0][0]-emt[1][0], emt[0][1]-emt[1][1], emt[1][0]-emt[0][0], emt[1][1]-emt[0][1]) < 0 or
            dot(emt[1][0]-emt[2][0], emt[1][1]-emt[2][1], emt[2][0]-emt[0][0], emt[2][1]-emt[0][1]) < 0
        ):
            print('Dunkak2Triangle')
        elif (
            dot(emt[0][0]-emt[1][0], emt[0][1]-emt[1][1], emt[2][0]-emt[0][0], emt[2][1]-emt[0][1]) == 0 or
            dot(emt[0][0]-emt[1][0], emt[0][1]-emt[1][1], emt[1][0]-emt[0][0], emt[1][1]-emt[0][1]) == 0 or
            dot(emt[1][0]-emt[2][0], emt[1][1]-emt[2][1], emt[2][0]-emt[0][0], emt[2][1]-emt[0][1]) == 0
        ):
            print('Jikkak2Triangle')
        else:
            print('Yeahkak2Triangle')
    else:
        leng.remove(long)
        if long**2 == leng[0]**2 + leng[1]**2:
            print('JikkakTriangle')
        elif long**2 > leng[0]**2 + leng[1]**2:
            print('DunkakTriangle')
        else:
            print('YeahkakTriangle')