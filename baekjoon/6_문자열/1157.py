s = input().lower()
s2 = list(set(s)) #중복제거
c = 0
for i in s2: #중복 제거된 리스트 돌면서
    if c<s.count(i): #중복 제거 안된 문자열에서 개수 세기
        c=s.count(i)
        ans = i.upper()
    elif c==s.count(i): #elif를 조심하자. if가 실행되지 않았을때 elif가 실행될 수 있는것!
        c=s.count(i)
        ans = '?'
print(ans)

