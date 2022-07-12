# 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램

A, B = map(int, input().split())
if A>B:
    print(">")
elif A==B:
    print("==")
elif A<B:
    print("<")

# 새롭게 알게된 if 조건 한줄로 표현하는 방법(조건부표현식)
a, b = input().split()
a, b = int(a), int(b)
# a<b가 참이면 <, 그게 아니고 a>b가 참이면 >, 둘 다 아니면 ==
print('<'if(a<b)else'>'if(a>b)else'==')

# 조건부표현식 예제
ko = ['ㄱ', 'ㄴ', 'ㄷ']
#if 조건이 참이면 if 앞 문장, 거짓이면 else 뒷문장
print("ㄱ있어요." if 'ㄱ' in ko else "ㄱ없어요.")
# --> 결과 : ㄱ있어요.