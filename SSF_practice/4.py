a = [1,2,3,4]
while(len(a) != 0) :
    print(a[0])
    if(len(a) > 0) :
        a = a[1:len(a)]
    else :
        print(a.pop())