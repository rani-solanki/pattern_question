val=65
i=0
while(i<5):
    j=0
    while(j<i+1):
        ch=chr(val)
        print(ch,end=" ")
        j=j+1
    val=val+1
    print(" ")
    i=i+1