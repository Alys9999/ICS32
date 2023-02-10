def inputa():
    'take a valid input'
    while True:
        first=input()
        if first:
            com0=first[0]
            i=first.find("-n")
            com1=""
            path=""
            filename=""
            if i != -1:
                com1=first[i:i+2]
                try:
                    path=first[2:i-1]
                    filename=first[i+3:]
                except IndexError:
                    print("invalid input")
                    pass
            if path=="":
                path=first[2:]
            lis=[com0,path,com1,filename]
            break
        else:
            print("invalid input")
            pass
    lis2=[]
    for i in lis:
        if i:
            lis2.append(i)
            
    return lis2

i=inputa()
print(i)