# 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램
import sys

# set 이용 # set 타입은 중복이 불가능 하며, 튜플이다. 또한 set으로 바꾸면 순서를 오름차순으로 정리한다.
n = []
for _ in range(10):
    i = int(sys.stdin.readline().rstrip())
    n.append(i%42)
cnt = list(set(n)) 
print(cnt)
print(len(cnt))

# for 반복 이용
arr = [1,2,3,3,4,5,5,5,6,7]
result = [] #중복 제거된 값 들어갈 리스트
for value in arr:
    if value not in arr: # arr 요소가 result에 없으면
        result.append(value) #result에 추가
print(result)

# dictionary 이용 # 딕셔너리의 키 값은 중복 불가 성질이 있음.
arrr = [1,2,3,4,4,4,4,5,5,6,6,7]
result1 = dict.fromkeys(arrr) #dict.fromkeys(iterable) : 인자로 들어온 iterable 데이터를 key 값으로 해서 딕셔너리 자료형을 만들어주는 메소드
print(result1)
result2 = list(result1) # == list(dict.fromkeys(arrr))
print(result2) # result1의 키 값들만 리스트로 만듦.