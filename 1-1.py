head ="python"
tails ="is fun"
print(head+tails)   #head 와 tails 의 합
len(head)   #head의 길이
a = "Life is too short, you need python!"
print(a[3]) #a의 3번쨰 문자 출력
a = "20210726.sunny"
print(a[0:8])   #a의 0에서 8번째까지
print(a[:8])    #위에것과 같은역할
q = "pithon"    #잘못된 문자
q =q[:1] +'y'+q[2:]    #문자열을 쪼갠후 y 추가
print(q)
num = 3 #문자열 아님
b = "i ate %d apples"
print(b %num)   #b에 num(3) 대입(여러개 가능) 예 = %(num1,num2)