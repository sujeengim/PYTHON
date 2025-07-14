from collections import deque

n, k = map(int, input().strip().split())
q = deque(range(1, n+1))
anslist = []

while len(q) > 1:
    q.rotate(-(k-1))
    anslist.append(q.popleft())
anslist.append(q.popleft())
'''
rotate
n이 양수면 → 오른쪽으로 n칸 회전
n이 음수면 → 왼쪽으로 n칸 회전
시간복잡도는 O(k)
'''

print(f"<{', '.join(map(str, anslist))}>")
