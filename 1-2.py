a = "Life is too short \n sunny"
print(a)
print("i ate %s apples" %3.567) #문자열로 인식함
print("Error is %d%%" %98)  #%% = %출력
print("%10s" %"gd") #오른쪽 정렬
print("%-10s" %"gd")    #왼쪽 정렬
print("%0.4f" %3.98765) #소수 출력
print("%10.4f" %3.542896)
#format
print("i eat {0} apples" .format(4))    #format를 이용해 4를 출력
num=720
min=10
s='8시 20분'
print("오늘 {0}번 버스가 {1}분 늦게 왔다 그래서 나는 {2}에 학교에 도착했다" .format(num,min,s))
#정렬
print("{0:<10}".format("gd"))   #왼쪽정렬
print("{0:>10}".format("gd"))   #오른쪽 정렬
print("{0:^10}".format("gd"))   #중앙 정렬
#정렬 후 기호 추가
print("{0:=^10}".format("gd"))
print("{0:!<10}".format("gd"))
#format간단히 사용하기
name='홍길동'
age=50
print(f'나의 이름은 {name} 입니다, 나는 {age}살 입니다')    #name, age 대입
#정렬
print(f'{"gd":<10}')    #왼
print(f'{"gd":>10}')    #오
print(f'{"gd":^10}')    #중앙
#정렬 후 기호 추가
print(f'{"gd":!<10}')
print(f'{"gd":=^10}')
#예제
print("{0:!^12}".format("python"))
print(f'{"python":!^12}')
#대(소)문자로 변경
d='imga'
print(d.upper())
print(d.lower())
#공백 제거
a='    gd    '
print(a.lstrip())
print(a.rsplit())
print(a.split()) 