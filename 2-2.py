#조건문 2
#while
treehit = 0
while treehit <10:
    treehit=treehit+1
    print("%d번 찍었다" %treehit)
    if treehit ==10:
        print("나무 넘어감")
#while 과 break
coffee=10
while True:
    money = int(input("돈을 넣어주세요:"))  #문자 입력받기
    if money ==300:
        print("커피 주기")
        coffee -=1
    elif money >300:
        print("거스름돈 %d 원 주고 커피 주기" %(money-300))
        coffee-=1
    else:
        print("돈을 다시 돌려주고 커피를 안줌")
        print("남은 커피는 %d 입니다" %coffee)

    if coffee==0:
        print("커피를 모두 팔아 판매를 중지함")
        break
#continue
a=0
while a<10:
    	a+=1
	if a%2==0: continue #짝수일때 건너뜀
	print(a)
#for
list=['one','two','three']
for i in list:
    print(i)

marks=[90,25,67,45,88]
for i in marks:
    if i >=60:
        print("합격")
    else:
        print("불합격")
#range
a=range(1,11)
add=0
for i in range(1,11):
	add+=i
print(add)

marks=[90,25,67,45,88]
for number in range(len(marks)):
	if marks[number]<60: continue
	print("%d 번 학생 합격을 축하함" %(number+1))

for i in range(2,10):
    	for j in range(1,10):
		    print("%d * %d = %d" %(i,j,i*j))
#list와 for
a=[1,2,3,4]
res=[]
for i in a:
   	if i%2==0:
        	res.append(i*3)
print(res)