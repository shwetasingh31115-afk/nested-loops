num=int(input("Enter a number:"))
t=num
numlen=1
while t>0:
    numlen+=1
    t=int(t/10)
if numlen>=4:
    numlen=int(num/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numlen:
                midone=rem
        elif chk==(numlen-1):
             midtwo=rem
        num=int(num/10)
        chk+=1
    prod=midone*midtwo
    print(prod)
else:
     print("its not an 4 or more than 4digit number")