n = list(input().split())
# " I=input().split() " == " sorted(I) "
n = ''.join(n)

a = sorted(n)
a = ''.join(a)
d = sorted(a, reverse=True)
d = ''.join(d)

if n == a:
    print('ascending')
elif n == d:
    print('descending')
else:
    print('mixed')