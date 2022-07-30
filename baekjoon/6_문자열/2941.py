two = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()

for i in two:
    if i in s:
        s=s.replace(i, '?', -1)
        # 문자열.replace(old, new, [count])
        # replace 함수는 문자열에 있는 old문자를 new문자로 변경한다
        # count는 선택이며, count 수만큼 변경한다. 기본값은 전체를 의미하는 -1이다.(count 비워두면 문자열 전체 변경)
print(len(s))