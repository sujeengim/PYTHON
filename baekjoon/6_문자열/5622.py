s = input()
count=0
for i in s:
    count+=2
    if 65<=ord(i):
        count+=1
    if 68<=ord(i):
        count+=1
    if 71<=ord(i):
        count+=1
    if 74<=ord(i):
        count+=1
    if 77<=ord(i):
        count+=1
    if 80<=ord(i):
        count+=1
    if 84<=ord(i):
        count+=1
    if 87<=ord(i):
        count+=1
print(count)