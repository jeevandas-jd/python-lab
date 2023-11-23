n=int(input("enter a number \n>>>"))
tmn=n
tmn1=n
tmn2=n
tmn3=n
nd=0
while tmn != 0:
    tmn=tmn//10
    nd=nd+1
sum=0
reverse=0
diff=0
for i in range(n):
    sum=sum+(tmn1%10)
    tmn1=tmn1//10
print(f"sum of digits         = {sum}")
for j in range(nd):
    reverse=(reverse*10)+tmn2%10
    tmn2=tmn2//10
print(f"reverse of the number = {reverse}")
#subquestion 3
odd,even=1,1
for k in range(1,nd+1):
    if k%2==0:
        even=even*(tmn3 % 10)
        tmn3=tmn3//10
    else:
        odd=odd*(tmn3 % 10)
        tmn3 = tmn3 // 10
print(f"diffrence between the product of digits at odd position and  product of digits at even position = {even-odd}")








