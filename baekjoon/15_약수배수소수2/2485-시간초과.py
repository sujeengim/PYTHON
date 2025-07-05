mport sys, math
        
def main():
    n = int(input()) #아래 모두 O(1)
    originlist = [] 
    checklist = []
    cnt = 0
    
    for i in range(n): #(n)회 반복
        originlist.append(int(sys.stdin.readline())) #O(1)

    for i in range(len(originlist)-1): #(n)회 반복
        checklist.append(originlist[i+1] - originlist[i]) #O(1)

    check = math.gcd(*(checklist)) #간격들의 최대공약수 

    for i in range(originlist[0], originlist[-1]+1, check): # (n / check)회 반복
        if i not in originlist: #O(n)
            cnt += 1 #O(1)
    # ==> O(n^2 / check)

    print(cnt)


if __name__ == "__main__":
    main()
