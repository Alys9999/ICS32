def project0():
    x=int(input())
    print("+-+\n| |\n+-+",end="")
    for i in range(1,x):
        print("-+")
        print(i*2*(" "),end="")
        print("| |")
        print(i*2*(" "),end="")
        print("+-+",end="")
    

project0()