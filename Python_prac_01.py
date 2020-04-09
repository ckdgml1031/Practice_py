#useageof python


#if01
a=15
if a>5:
    a=a-10
print(a)

#if02
a,b = 10,20
if a>b:
    cha = a-b
    print(cha)
else:
    cha = b-a
    print(cha)
#if03
a,b = 21,10

if a%2==0:
    if b%2==0:
        print("둘다짝")
    else :
        print("a짝,b홀")
else :
    if b%2==0:
        print("a홀,b짝")
    else :
        print("둘다홀")
