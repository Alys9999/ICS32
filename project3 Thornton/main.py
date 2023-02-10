import netp as n
import tool as t
import baselogic as b



        
def center():
    input1=t.inputOne()
    if input1[0]=="NOMINATIM":
        center=n.nomigetc(input1[1])
    elif input1[0]=="FILE":
        center=b.cfilelist(input1[1])
    return center
    
