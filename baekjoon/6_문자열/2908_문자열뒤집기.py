# 슬라이싱
n1, n2 = (input().split())
n1 = int(n1[::-1])
n2 = int(n2[::-1])
print(n1 if n1>n2 else n2)

# for 반복
n1, n2 = input().split()
nn1, nn2 = [], []
print(nn1, nn2)
for i in n1:
    nn1 = i + nn1 #빈리스트에 앞 숫자를 뒤로 보내며 저장하기
for i in n2:
    nn2 = i + nn2

# 리스트 reverse 이용
s = "reverse test" # reverse -> tset esrever
s = list(s)
print(s) # 리스트변환 출력
s.reverse() #reverse 메소드 . 변수에 또 담지 않아도 s자체가 역순으로 바뀜.
print(s)

s = ''.join(s) #리스트를 문자열로 변환
print(s)