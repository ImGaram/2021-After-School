#함수 def
def add(a,b):
    	return a+b
a=5
b=10
c=add(a,b)
print(c)
#함수와 for 그리고 많은 변수 넣기
def add_many(*args):
    	res=0
	for i in args:
		    res+=i
	return res
result = add_many(1,2,3,4,5,6,7,8,9)
print(result)
#여러 return 값
def add_mul(a,b):
	return a+b,a*b
res=add_mul(7,8)
print(res)

def add_mul(a,b):
    	return a+b
        return a*b  #출력 안됨
res=add_mul(7,8)
print(res)
#특정 값만 받는 함수
def say(imga):
    	if imga=='stupid':
		    return  #아무 값도 리턴 안함
	print("나의 별명은 %s 입니다" %imga)
print('ㅄ')