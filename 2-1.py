  #조건문
money = 3000
card=False
if money<=3000 or card: #money가 3000원 이상 또는 카드가 있음
    print("taxi")
else:
    print("walk")
#in/not in
x=3
y=4
print(x<y)  #3<4
print('a' not in ['a','b','c','d']) #a가 있음
print(sep='\n')
#pass
pocket = ['paper','phone','B','EAR','mask','card']
if 'money' in pocket:
	print("taxi")
elif 'card' in pocket:  #c의 else if
	pass    #조간이 여기에 걸리지만 아무것도 살향 안하고 끝나버림
else:
	print("run")