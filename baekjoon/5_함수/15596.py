def solve(a):
    '''정수 n개의 합'''
    sigma=0
    for i in a:
        sigma += i
    return sigma

def solve2(a):
    return sum(a)

a = list(map(int, input().split()))
print(solve2(a))