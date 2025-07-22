# # 1764
import sys

nolisten, nolook = map(int, input().strip().split())
min = min(nolisten, nolook)
nolistenset = set()
nolookset = set()
nolistenlookset = set()

for _ in range(nolisten):
    nolistenset.add(sys.stdin.readline().strip())

for _ in range(nolook):
    nolookset.add(sys.stdin.readline().strip())

for i in sorted(nolistenset):
    if i in nolookset:
        nolistenlookset.add(i)

print(len(nolistenlookset))
print(*(nolistenlookset), sep='\n')

# list1 = [1,2,3]
# list2 = [1,2,3,4]
# print(min(list1, list2))
