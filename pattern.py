a=int(input("enter lines="))
v=1
print(v)
while a>1:
    ab=""
    while v>0:
        c=v%10
        count=1
        v//=10
        while v>0 and v%10==c:
            count+=1
            v//=10
        ab=str(count)+str(c)+ab
    print(ab)
    v=int(ab)
    a-=1