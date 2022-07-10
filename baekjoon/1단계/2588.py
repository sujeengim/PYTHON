# 곱셈 과정 값 구하기

n1, n2 = [input() for _ in range(2)]
answer =[]
for i in range(2,-1,-1):
    for k in range(2,-1,-1):
        if (int(n1[k])*int(n2[i]))//10 != 0:
            answer.append((int(n1[k])*int(n2[i]))%10)
        else:
            answer.append(int(n1[k])*int(n2[i]))
    print(answer.sort(reverse=True))        
print()