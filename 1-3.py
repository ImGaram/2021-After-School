#list
#c의 구조체 와 비슷함

a = [1,2,3,4,5]
a.append(6) #숫자(문자) 추가
print(a)
b = [1,2,['life','is'],3,4,5]
print(b[2])
print(len(b))   #life,is 를 하나로 취급함
#중첩된 리스트
a=[1,2,['a','b',['life','is']]]
print(a[2][2][0])   #2번째 리스트(a,b,[life,is])의 2번째(life,is)의 0번째(life)
b = [1,2,3,4,5]
print(b[0:2])   #b list의 0~2 번째 수까지 출력
print(b[:2])    #처음부터 1번째 수까지
print(b[2:])    #3번째부터 끝까지
#리스트의 수정과 삭제
#리스트 값 수정
a=[1,2,3,4,5]
a[2] = 4
print(a)
#리스트 요소 삭제
del a[4]
print(a)
#슬라이싱 기법으로 여러개 추가, 삭제 가능
#리스트 요소 추가
a.append(5) #리스트의 맨 마지막에 5 추가
a.append([6,7]) #리스트의 맨 마지막에 [6,7] 추가
#리스트 정렬
a=[1,4,3,2]
a.sort()
print(a)
#문자도 가능함
#리스트 내림차순으로 정렬
a=['a','c','b']
a.reverse()
print(a)
#리스트 위치 변화
a=[1,2,3]
a.index(3)
print(a)
a.index(1)
print(a)
#리스트에 요소 삽입
a=[1,2,3]
a.insert(0,4)
print(a)
#리스트 요소 제거
a = [1,2,3,1,2,3]
a.remove(3)
print(a)
