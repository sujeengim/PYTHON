# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램

score = int(input())
print('A' if(90<=score) else 'B' if(80<=score) else 'C' if(70<=score) else 'D' if(60<=score) else 'F')