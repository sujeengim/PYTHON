import random

print('숫자 게임 시작')
number = random.randrange(1, 100, 1) #start, stop, step
print('정답 미리보기: ', number)

while True:
  guess = int(input("1부터 100 사이 숫자를 추측해보세요: "))

  if number == guess:
    break
  else:
    print('틀렸습니다. 다시')

print('숫자 게임 종료')
