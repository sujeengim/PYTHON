import sys

n = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split())) 
#순서대로 답이 나와야해서 B는 오름정렬 하면 안됨

def binary(emt, a, start, end):
    if start > end:
        return 0
    mid = (start+end)//2 
    # 어떤범위(여기선 start~end) 사이의 중간값을 찾고싶으면 (범위시작값+범위끝값)//2
    if emt == a[mid]: #적중
        return 1
    elif emt > a[mid]:
        return binary(emt, a, mid+1, end)
    else:
        return binary(emt, a, start, mid-1)


for emt in B:
    start = 0
    end = len(A)-1
    print(binary(emt, A, start, end))