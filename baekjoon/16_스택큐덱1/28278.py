from typing import Any

class FixedStack:
    # 예외(Exception) 클래스
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity: int = 100000) -> None:
        self.stk = [None] * capacity # 리스트형 스택 본체
        self.capa = capacity  #스택 크기 : 스택 최대 개수
        self.ptr = 0 #스택 포인터 : 현재 쌓인 스택 개수 

    def push(self, value:Any) -> None:
        '''1 명령 해결'''
        if self.ptr >= self.capa: #용량 초과면
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> None:
        '''2 명령 해결'''
        if self.ptr <= 0: 
            raise FixedStack.Empty
        self.ptr -= 1
        print(self.stk[self.ptr])

    def print_len(self) -> None:
        '''3 명령 해결'''
        print(self.ptr)

    def is_empty(self) -> None:
        '''4 명령 해결'''
        print(int(self.ptr <= 0))

    def print_top(self) -> None:
        '''5 명령 해결'''
        if self.ptr <= 0:
            raise FixedStack.Empty
        print(self.stk[self.ptr-1])
    

mystack = FixedStack()

for _ in range(int(input())):
    command = list(map(int, input().strip().split()))
    try:
        if command[0] == 1:
            mystack.push(command[1])
        elif command[0] == 2:
            mystack.pop()
        elif command[0] == 3:
            mystack.print_len()
        elif command[0] == 4:
            mystack.is_empty()
        elif command[0] == 5:
            mystack.print_top()
        else:
            pass
    except FixedStack.Empty:
        print(-1)
    except FixedStack.Full:
        pass
