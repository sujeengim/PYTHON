from typing import Any

class FixedStack:
    # 예외(Exception) 클래스
    class Empty(Exception):
        print(-1)
    class Full(Exception):
        print("Full")

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity # 리스트형 스택 본체
        self.capa = capacity  #스택 크기 : 스택 최대 개수
        self.ptr = 0 #스택 포인터 : 현재 쌓인 스택 개수  -> 2,3,4,5에 사용

    def push(self, value:Any) -> None:
        '''1 명령 해결'''
        if self.ptr >= self.capa: #용량 초과?
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def print_stack() -> None:
        '''2 명령 해결'''
        if self.ptr <= 0: 
            raise FixedStack.Empty
        print(self.stk[:self.ptr-1])

    

    
