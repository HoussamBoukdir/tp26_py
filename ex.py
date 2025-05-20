n=int(input("donner un entier : "))
m=int(input("donner un entier : "))
if n>m :
    a=n
    n=m
    m=a
i=1
while i<=m :
    b=n%i
    c=m%i
    if c==0 and b==0 :
        d=i
    i+=1
print(f"le PGCD de {n} et {m} est : {d}")