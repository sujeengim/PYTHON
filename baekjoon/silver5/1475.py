import math

n = int(input())

nlst = [0]*10

for i in str(n):
    nlst[int(i)]+=1

nlst[6] = math.ceil((nlst[6]+nlst[9])/2)
nlst[9] = nlst[6]

print(max(nlst))