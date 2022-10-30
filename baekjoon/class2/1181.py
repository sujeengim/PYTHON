n=int(input())

lst = []

for i in range(n):
    lst.append(input())
lst = set(lst) #중복제거
lst = list(lst) #다시 리스트
lst.sort()  #사전순으로 정렬 후 
lst.sort(key = len) #길이로 다시 정렬

for i in lst:
    print(i)