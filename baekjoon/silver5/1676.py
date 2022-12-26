n = int(input())

def fac(a):
    if a==0:
        return 1
    return a*fac(a-1)

print('fac : ',fac(n))
rev_fac = str(fac(n))[::-1]
print('rev_fac : ', rev_fac)
cnt = 0

if rev_fac[0] != '0':
    print(0)
else:
    for i in range(len(rev_fac)):
        if rev_fac[i] == '0':
            cnt+=1
        else:
            ans = rev_fac[0:i]
            print(len(ans))
            break