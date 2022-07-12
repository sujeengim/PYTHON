# print문으로 문자열 표현하는 여러가지 방법

# 변환 문자 활용 
print("올해는 %d년 입니다." % 2022) # %d : 숫자 데이터
print("올해는 %d년, 내년은 %d년 입니다." % (2022, 2023))
print("나는 %s를 탑니다." % '지하철') # %s : 문자열 데이터(따옴표로 묶기)
print("Google은 %c로 시작합니다." % 'G') # %c : 문자 하나 데이터
a = '안녕' #문자열
b = '안' # 문자 하나, 문자열로도 가능
print("모두 %s" % a)
print("모두 %c녕" % b)
print("모두 %s녕" % b) 
print()

# format 활용
print("올해는 {}년 입니다.".format(2022))  #따옴표 다음에 .format()
print("올해는 {}년, 내년은 {}년 입니다.".format(2022, 2023))
print("나는 {}를 탑니다." .format('지하철')) 
print("Google은 {}로 시작합니다." .format('G')) 
a = '안녕'
b = '안'
print("모두 {}" .format(a))
print("모두 {}녕" .format(b))
print("모두 {}녕".format(b)) 
# {위치}로 해당 위치의 데이터를 받을 수 있음
print("{2}와 {0}와 {1}는 한 집에 삽니다.".format('철수','영희','바둑이'))
# print문 자체적으로 데이터 입력
print("우리 가게에는 {fruit3}과 {fruit1}와 {fruit2}이 있다.".format(fruit1='사과',fruit2='바나나',fruit3='포도'))
# 파이썬 3.6이상에서 변수를 바로 print에 사용 가능
boy = '철수'; girl='영희'; dog='바둑이'
print(f"{girl}와 {boy}는 {dog}와 한 집에 삽니다.")