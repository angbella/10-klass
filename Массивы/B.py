from random import randint
a=[ ]
a=[randint (0,100) for x range (5)]
sum1=0
sum 2=0
for x in a:
    if x<50:
        sum1+=x
        sred1=sum1//5
    else:
        sum2+=x
        sred2=sum2//5
print(sred1,sred2)
