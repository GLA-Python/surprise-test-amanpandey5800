from tkinter import N


def ex(n):
    d=n[1]-n[0]-1
    for i in range(1,len(n)):
        b=n[i+1]-n[i]
        i+=1
        if abs(b>d):
            d=b
            return True
        else:
            return False

n=list(map(int,input("enter list==").split()))
print(ex(n))
