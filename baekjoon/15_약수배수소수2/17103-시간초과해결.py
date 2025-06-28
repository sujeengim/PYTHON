import sys

# 에라토스테네스의 체
MAX = 1000000 #미리 소수를 구해두자
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False #True이면 소수

# 2부터 √MAX까지 반복하면서, i가 소수면:
# 그 **배수**들을 전부 소수 아님(False)으로 표시
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

# 입력
T = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(T)]

# 각 수에 대해 골드바흐 파티션 개수 세기
for n in nums:
    count = 0
    for i in range(2, n // 2 + 1): #n // 2 로 중복 제거
        if is_prime[i] and is_prime[n - i]: #n=i+primeX
            count += 1
    print(count)
