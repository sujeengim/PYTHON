while True:
    # t = list(map(int, input().split())).sort() 이게 왜 안돼
    t = list(map(int, input().split()))
    if t == [0,0,0]:
        break    
    max_num = max(t)
    t.remove(max_num)
    if ((t[0])**2 + (t[1])**2 == (max_num)**2):
        print('right')
    else:
        print('wrong')