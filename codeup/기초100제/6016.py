# [기초-입출력] 문자 2개 입력받아 순서 바꿔 출력하기2
# 공백을 두고 문자(character) 2개를 입력받아 순서를 바꿔 출력해보자.

# 처음 풀이
# a, b = input().split('') -> ''사이에 공백 없으면 밸류에러뜸.
# a, b = input().split() -> 가능
a, b = input().split(' ')
print(b,a)