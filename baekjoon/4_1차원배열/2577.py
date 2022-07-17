# 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램
import sys

# count 사용 x
num = [0 for _ in range(10)] # 0~9 쓰인 개수 저장. 여길 자꾸 range(9)라고 해서..
nums = [0 for _ in range(3)] # A, B, C 저장
ABC = 1
for i in nums:
    i = int(sys.stdin.readline().rstrip())
    ABC *= i
for i in str(ABC):
    for j in range(10): #여길 자꾸 range(9)라고 해서..
        if i==str(j):
            num[j] += 1
for i in num:
    print(i)


# count 사용 o
abc = 1
cnt = [0 for _ in range(10)]
for i in range(3):
    i = int(sys.stdin.readline().rstrip())
    abc *= i
abc = str(abc)
for i in range(10):
    cnt[i]=abc.count(i)
    print(cnt[i])