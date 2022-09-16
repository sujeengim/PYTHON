#반복문이 언제 끝나는지.

'''
1. 인수를 구한다
2. 소인수를 구한다
3. 소인수분해를 한다
'''

n = int(input())
n_test = n

# n_set = {}
n_set = []
# set(집합)
# 1. 순서가 없음 2. 중복 제거됨

'''1'''
for i in range(2,n):
    for j in range(2,n):
        if i*j == n and i not in n_set and j not in n_set:
            # n_set.update([i, j])
            n_set.append(i)
            n_set.append(j)
print(n_set) #n_set에 인수담기

'''2'''
n_list = list(n_set) #세트를 리스트로 변환
for i in n_list:
    for j in range(2,i):
        if i%j==0 and (i in n_list):
            n_list.remove(i)
print(n_list) # n_list에 소인수만 담기

'''3'''
n_test = n

n_list.sort() #리스트 오름차순 정렬
n_list_cnt = []

for i in n_list:
    cnt = 0
    while n_test/i != 0:
        cnt += 1
        n_test = n_test%i
    n_list_cnt.append(cnt)

print(n_list_cnt)
        
for i in range(len(n_list)):
    for _ in range(n_list_cnt[i]): #i값의 인덱스를 알아냄

        print(n_list[i])