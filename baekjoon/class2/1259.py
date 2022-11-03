while True:
    n = input()
    if n=='0':
        break
    if n[0] == '0':
        for i in range(1,len(n)):
            if n[i]!='0':
                n = n[i:]
                break
    n2 = n[::-1]
    if n2==n:
        print('yes')
    else:
        print('no')