def category(a):
    '''세 변의 길이를 담은 리스트를 a로 받는다'''
    print(a)
    scan_a = [x for x in a if x>1000]
    if len(scan_a) != 0:
        return print("세 변의 길이를 입력하세요.")

    a.sort()
    print(a)

    if a[-1]>=sum(a[:]):
        return print("Invalid")
    elif len(set(a)) == 1:
        return print("Equilateral")
    elif len(set(a)) == 2:
        return print("Isosceles")
    else:
        return print("Scalene")

while True:
    a = list(map(int, input().split(' ')))
    if sum(a)==0:
        break
    category()
