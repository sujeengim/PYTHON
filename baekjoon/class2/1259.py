while True:
    n = input()
    if n=='0':
        break
    n2 = n[::-1]
    if n2==n:
        print('yes')
    else:
        print('no')