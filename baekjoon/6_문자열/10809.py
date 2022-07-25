s=input()
for i in range(97,123):
    if chr(i) in s:
        # 인덱스 함수는 찾는 값이 리스트에서 가장 먼저 등장하는 곳의 인덱스번호를 알려줌
        print(s.index(chr(i)), end=' ')
    else:
        print(-1, end=' ')