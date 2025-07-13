# 2164 - 시간초과
'''
import time
start = time.time()

n = int(input())
nlist =[i for i in range(1, n+1)]

for _ in range(len(nlist)-1):
    #1. 버린다
    del nlist[0]
    #2. 옮긴다
    nlist.append(nlist.pop(0))


print(nlist[0])
print("Time: ", time.time() - start)
'''
'''
1. 어디서 시간이 많이 걸리는가?
   - 리스트의 첫 번째 요소를 삭제하는 것은 O(n) 시간 복잡도를 가지므로, 전체 과정은 O(n^2)
2. 어떻게 개선할 수 있는가?
    - deque는 append와 popleft 연산이 O(1) 시간 복잡도를 가지므로, 
    리스트 대신 deque를 사용하면 시간 복잡도를 O(n)으로 줄일 수 있다.
'''

# 2164 개선된 코드
from collections import deque

n = int(input())
nlist = deque([i for i in range(1, n+1)])

while len(nlist) > 1:
    nlist.popleft()  
    nlist.append(nlist.popleft())  # 두 번째 요소를 마지막으로 이동

print(nlist[0])
