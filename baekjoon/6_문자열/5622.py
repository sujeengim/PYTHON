# s = input()
# count=0
# for i in s:
#     count+=2
#     if 65<=ord(i):
#         count+=1
#     if 68<=ord(i):
#         count+=1
#     if 71<=ord(i):
#         count+=1
#     if 74<=ord(i):
#         count+=1
#     if 77<=ord(i):
#         count+=1
#     if 80<=ord(i):
#         count+=1
#     if 84<=ord(i):
#         count+=1
#     if 87<=ord(i):
#         count+=1
# print(count)

# 딕셔너리 같은 튜플..?
# dial={
#     ('2','ABC'),
#     ('3','DEF'),
#     ('4','GHI'),
#     ('5','JKL'),
#     ('6','MNO'),
#     ('7','PQRS'),
#     ('8','TUV'),
#     ('9','WXYZ'),
#     }
# S = input()
# count=0
# for i in S:
#     for j in dial:
#         if i in j[1]:
#             count+=(int(j[0])+1)
# print(count)

# 딕셔너리 사용 ... 더 생각해보기
dial2 ={
    'ABC':2,
    'DEF':3,
    'GHI':4,
    'JKL':5,
    'MNO':6,
    'PQRS':7,
    'TUV':8,
    'WXYZ':9
}
s= input()
count=0
for j in s:
    for i in dial2.keys():
        if s in i:
            count+=(dial2.get(i).values)+1
            print(dial2[i].values)
print(count)
# for i in s:
#     for j in dial2:
#         if i in dict.values[j]: