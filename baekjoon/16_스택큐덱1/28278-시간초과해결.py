#int(input())으로 인한 시간초과 문제를 sys.stdin.readline()로 해결
import sys

n = int(sys.stdin.readline()) 
stack = [] 

for _ in range(n):
    command_parts = sys.stdin.readline().split()  # 리스트로 저장됨

    if command_parts[0] == '1':
        stack.append(int(command_parts[1]))
    elif command_parts[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif command_parts[0] == '3':
        print(len(stack))
    elif command_parts[0] == '4':
        if stack:
            print('0')
        else:
            print('1')
    elif command_parts[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print('-1')
