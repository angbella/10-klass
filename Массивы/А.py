from random import randint
a=[ ]
a=[randint (0,100) for x in range (100)]
sum=0
for x in a:
    sum+=x
    sred=sum//2
print (sred)
