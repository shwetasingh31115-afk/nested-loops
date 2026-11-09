word=input("Enter your own word:")
char=input("Enter your own character:")
i=0
count=0
while i<len(word):
    if(word[i]==char):
        count+=1
    i=i+1
print(count)