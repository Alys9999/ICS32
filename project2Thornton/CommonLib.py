import ConnectFour as C



def F(col,row):
    newb=C.new_game(col,row)
    newb2=exc(newb.board)
    printb(newb2,newb.turn)
    return newb
    
def proc(newb,co):
    a=dec(newb,co)
    a2=exc(a.board)
    printb(a2,a.turn)
    return a





def col0():
    while True:
        col=input("please specify the column number from 4 to 20:")
        if col.isdigit():
            col=int(col)
            return col
        else:
            print("invalid input")
    
def row0():
    while True:
        row=input("please specify the row number from 4 to 20:")
        if row.isdigit():
            row=int(row)
            return row
        else:
            print("invalid input")


'''print the graphic accroding to ob'''
def forS(ofb):
    for i in ofb:
        print("")
        for j in i:
            pei(j)

'''print each item'''
def pei(s):
    if s==0:
        print(". ",end="")
    elif s==1:
        print("R ",end="")
    elif s==2:
        print("Y ",end="")

'''print whose turn'''
def forT(oft):
    if oft==1:
        print("Now is red turn")
    if oft==2:
        print("Now is yellow turn")

        
def printb(ofb,oft):
    forS(ofb)
    forT(oft)

            
def exc(board):
    '''exchange the 1 and 2 dimension of a 2d list'''
    board2=list(map(list,zip(*board)))
    return board2


def dpn():
    while True:
        co=input("drop or pop with a space and col number:")
        while True:
            colist=co.split(" ")
            try:
                if colist[0]=="drop" or "pop" and colist[1].isdigit():
                    return co
                else:
                    print("invalid input")
                    break
            except IndexError:
                print("invalid input")
                break

def dec(game_state,co):
    while True:
        try:
            colist=co.split(" ")
            if colist[0]=="drop" and colist[1].isdigit():
                rc=int(colist[1])-1
                a=C.drop(game_state,rc)
                return a
            elif colist[0]=="pop" and colist[1].isdigit():
                rc=int(colist[1])-1
                a=C.pop(game_state,rc)
                return a
        except:
            return dec(gamestate,dpn())

    
    
def we(gs):
    if C.winner(gs)==1:
        return str("RED is winner")
    elif C.winner(gs)==2:
        return str("YELLOW is winner")


        


            
                

            
