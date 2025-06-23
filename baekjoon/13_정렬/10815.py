# import sys

# def len_check(x):
#     if len(nlist) > 500000 or len(mlist) > 500000:
#         print("입력 범위가 아닙니다.")
#         sys.exit()

# def range_check_int(x):
#     if (x < 1) or (x > 500000):
#         print("입력 범위가 아닙니다.") 
#         sys.exit()   

# def range_check_list(xlist):
#     for xscan in xlist:
#         if xscan < -10000000 or xscan > 10000000:
#             print("입력 범위가 아닙니다.")
#             sys.exit()


def contain(nlist, mlist):
    for mscan in mlist:
        if mscan in nlist:
            print(1, end=' ')
        else :
            print(0, end=' ')

n = int(input())
nlist = set(map(int, input().strip().split(' ')))
m = int(input())
mlist = list(map(int, input().strip().split(' ')))
# mlist의 중복은 프로그램 실행에서 시간이 오래걸린다는 단점 존재
# 시간 초과된 입력 받기 
# nlist = list(dict.fromkeys(list(map(int, input().strip().split(' ')))))
# mlist = list(dict.fromkeys(list(map(int, input().strip().split(' ')))))

# 아래 검사는 이미 완료된 상태라 가정함
# len_check(n)
# len_check(m)
# range_check_int(n)
# range_check_int(m)
# range_check_list(nlist)
## mlist의 범위도 확인해야 하지만 프로그램 실행에서 중요하지 않음

contain(nlist, mlist)
