def details():
    name=input("enter name\n>>>")
    code=input("enter employee code\n>>>")
    bs=int(input("enter basic payment\n>>>"))
    return name,code,bs
def sal(s):
    da,hra,ma,pt,it=0,0,0,0,0
    if s<10000:
        da=(s*5)/100
        hra=(s*(2.5))/100
        ma=500
        pt=20
        pf=(s*8)/100
        it=0
    elif s<30000:
        da=(s*(7.5))/100
        hra=(s*(5))/100
        ma=2500
        pt=60
        pf=(s*8)/100
        it=0
    elif s<50000:
        da=(s*11)/100
        hra=(s*(7.5))/100
        ma=5000
        pt=60
        pf=(s*11)/100
        it=11
    else:
        da = (s * (25)) / 100
        hra = (s * (11)) / 100
        ma = 7000
        pt = 80
        pf = (s * 12) / 100
        it = 20
    gs=s+da+hra+ma
    d=pt+pf+it
    net=gs-d
    print(f'_____BILL____\nBasic pay:{s}\nDA       :{da}\nHRA      :{hra}\nMA       :{ma}\nPT       :{pt}\nPF       :{pf}\nIT       :{it}\n_____netpay____\nDIDUCTION :{d}\nGROSSALARY:{gs}\nNET SALARY:{net}')
n,c,b=details()
sal(b)