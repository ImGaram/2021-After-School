#q1
a="Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#shirt
#q2
res=0
i=1
while i<=1000:
    if i%3==0:
        res+=1
    i+=1
print(res)
#q3
for i in range(1,6):
    for j in range(1,6):
        if j<=i:
            print("*",end="")
    print(sep='\n')
#q4
for i in range(1,101):
    print(i)
#q5
l=[70,65,55,75,95,90,80,80,85,100]
tot=0
for score in l:
    tot+=score
avg =(tot/10.0)
print(avg)