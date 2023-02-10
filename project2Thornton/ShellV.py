import CommonLib as C
import ConnectFour as CF

'''using function from CommonLib to construct a shell only version'''
'''add the column number sign'''

def lp():
    col=C.col0()
    row=C.row0()
    co=dpn()
    x=C.proc(C.F(col,row),co)
    while True:
        co=dpn()
        x=C.proc(x,co)
        if CF.winner(x)!=0:
            C.we(x)
            break
        
        

if __name__=="__main__":
    lp()