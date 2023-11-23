def substring(s):
    se=[]
    for i in range(len(s)):
         for j in range(i+1,len(s)+1):
            se.append(s[i:j])
        #print(el)
    return se
def ktimes(s,n):
    se=[]
    for i in range(len(s)):
         for j in range(i+1,len(s)+1):
            se.append(s[i:j])
    for el in se:
        if len(el)==n:
            print(el)
def distinct():
    se=[]
    for i in range(len(s)):
         for j in range(i+1,len(s)+1):
            se.append(s[i:j])
    for el in se:
        if len(el)!=n:
            se.remove(el)r
    ls=se
    for k in se:
        for m in range(len(k)):
            for n in range(len(k)):
                if k[m]==k[n] and m != n:
                    ls.remove(k)
    print(ls)





        #print(el)
a = input('enter a string \n>>>')
print(substring(a)