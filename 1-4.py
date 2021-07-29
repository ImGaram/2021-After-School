#튜플
t1 = (1,2,3)    #리스트와 차이점 : 요소 뒤에 ,를 붙여야함, 괄호 생략 가능
#튜플은 수정이 불가함
#튜플 다루기
t1 = (1,2,'a','b')
t2 = (3,4,5)
#인덱싱
print(t1[0])
print(t2[2])
#슬라이싱
print(t1[1:])
print(t2[:2])
#합과 곱
print(t1+t2)
print(t1*3) #튜플 * 튜플 불가능
#딕셔너리
dic={'name':'imga','phone':'01066376117','birth':'1206'}    #key = name,phone,birth  value = imga,01066..,1206
#딕셔너리 추가,삭제
dic[5]='asdf'   #key에 숫자를 넣을 수 있다
print(dic)
print(sep='\n')
del dic[5]  #key가 5인 key,value 삭제
print(dic)
#활용
#key로 value 얻기
dic[4]='temp'
print(sep='\n')
print(dic['name'])  #dic 의 name의 이름을 가진 key의 value 값
print(dic['birth'])
print(dic[4])
#b={1:'a',1:'b'}    딕셔너리의 key값은 중복되면 안됨
#a={[1,2]:'gd'}     리스트는 key값으로 쓸 수 없음
#딕셔너리 관련 함수
#key 리스트 만들기(keys)
print(sep='\n')
a={1:'a',2:'b',3:'c',4:'d',5:'e'}
print(a.keys())     #dict_keys객체에 저장, 리스트의 기능과 같다
#value 리스트 만들기(values)
print(a.values())   #dict_values객체에 저장
#key, value 쌍 얻기(items)
print(a.items())    #dict_items객체에 저장, 리스트의 기능과 같다
#key,value 모두 지우기(clear)
print(a.clear())
#key로 value 얻기(get)
c={'name':'imga','phone':'01066376117','birth':'1206'}
print(c.get('name'))    #c['name'](이렇게도 가능함
#집합
s1=set([1,2,3]) #set은 집합을 만드는 함수이다
s2=set([3,4,5,6])
s3=set("Hello")
print(sep='\n')
print(s3)   #순서 없음, 중복혀용 X
#변환(list - tuple)
l1 = list(s1)
print(sep='\n')
print(l1)
l2=tuple(s1)
print(l2)
s1=set(s1)
print(s1)
#교집합
print(sep='\n')
print(s1&s2)    #중복되는 값
print(s1.intersection(s2)) #같은 역할
#합집합
print(s1|s2)    #중복되는 값은 하나씩 표현
print(s1.union(s2)) #같은 역할
#차집합
print(s1-s2)    #중복되지 않는 작은 값
print(s1.difference(s2))    #같은 역할
#집합 자료형 관련 함수
#add(값 추가)
print(sep='\n')
s1=set([1,2,3])
s1.add(4)
print(s1)
#update(값 여러개 추가)
s1.update([5,6])
print(s1)
#remove(값 제거)
s1.remove(2)
print(s1)
print(sep='\n')
#bool 자료형
a=True
b=False
print(a==b)
print(a!=b)
#bool 연산
print(sep='\n')
print(bool('python'))   #빈 문자열이 아니므로 true
print(bool('')) #빈 문자열이므로 false
print(sep='\n')
#변수
#예
a=1
b='python'
c=[1,2,3]
print(id(a))    #변수가 가리키는 메모리 주소
b=a #변수 복사숫자 밖
print(b,id(b))  #id 값이 a와 같아짐
print(a is b)   #a와 b가 같은가?
#변수를 만드는 방법
#변수 숫자 바꾸기
a=3
b=5
a,b = b,a
print(a,b)