def happy():
    n=int(input("enter a positive intiger\n>>>"))
    tmn2,tmn3=n,n
    it=0
    while it != 100:
        nd=0
        while tmn2 !=0:
            tmn2=tmn2//10
            nd=nd+1
        sum=0
        for i in range(nd):
            sum=sum+((tmn3%10)**2)
            tmn3=tmn3//10
        if sum==1:
            print("happynumber")
            it=100
        else:
            tmn2,tmn3=sum,sum
            it=it+1
        if it==99 and sum != 100:
            print("the number not happy!!")
happy()








