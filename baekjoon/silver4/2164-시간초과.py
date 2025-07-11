# import time
# start = time.time()

n = int(input())
nlist =[i for i in range(1, n+1)]

for _ in range(len(nlist)-1):
    #1. 버린다
    del nlist[0]
    #2. 옮긴다
    nlist.append(nlist[0])
    del nlist[0]

print(nlist[0])
# print("Time: ", time.time() - start)
