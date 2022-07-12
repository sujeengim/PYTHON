# 곱셈 과정 값 구하기

n1, n2 = [input() for _ in range(2)]
# [input() for _ in range(2)] 의미 :
# 줄바꿔 입력을 받기 위해 처음에 input.split('\n')으로 작성했었는데, ValueError.
# input은 한 줄만을 읽기 때문에 두 줄 이상의 값을 받아들일 수 없고, 따라서 줄바꿈 기호에 의한 구분도 존재하지 않는다.
# 여러 줄 값을 입력받으려면 input을 여러번 반복하는 for in 구문을 이용해야 함.
# 반복되는 입력값들을 리스트로 정리해야 하기에 대괄호 사용함.

print(int(n1)*int(n2[2])) # 숫자는 n2[0]이렇게 못함.
print(int(n1)*int(n2[1]))
print(int(n1)*int(n2[0]))
print(int(n1)*int(n2))