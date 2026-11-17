num=int(input("enter a number more than 1 digit:"))
binary=""
while num>0:
    rem=num%2
    for i in range(1):
        binary=str(rem)+binary
        num=num//2
print(binary)