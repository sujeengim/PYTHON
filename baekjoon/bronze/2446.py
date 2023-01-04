n = int(input())

#홀수로 출력

for b, s in zip(range(0,n), range(n,0,-1)):
    print(' '*b, '*'*(2*s-1), ' '*b, sep='')
for b, s in zip(range(n,0,-1), range(0,n)):
    print(' '*b, '*'*(2*s-1), ' '*b, sep='')