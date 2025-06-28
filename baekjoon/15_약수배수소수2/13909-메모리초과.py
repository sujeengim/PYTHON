def setDoor(n)->None:
    nlist = [False]*n
    for i in range(1,n+1):
        for j in range(i, n + 1, i): #배수 위치 값 뒤집기 
            nlist[j-1] = not nlist[j-1]

    print(sum(nlist))
    

def main()->None:
    n = int(input())
    setDoor(n)


if __name__ == "__main__":
    main()
