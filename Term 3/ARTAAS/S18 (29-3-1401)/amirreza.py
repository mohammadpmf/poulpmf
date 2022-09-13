from random import randint

def build_borad():
    borad = []
    for i in range(9):
        block=[["","","","",""],
        ["","","","",""],
        ["","","","",""]]
        borad.append(block)
        return borad
def row_availble(block , row , borad , num ):
    boradRow = int(block / 3)
    good = True
    for b in range(boradRow * 3 , (boradRow * 3) + 3 ):
        if b != block:
            if num in  borad[b][row]:
                good =False
                break
            return good
def col_available(block, row, col, board, num): 
    boardCol = block % 3
    good = True
    for b in (boardCol, boardCol + 3, boardCol + 6):
        if b != block:
            if num == board[b][row][col]:
                good = False
                break
            return good
def fill_borad(board):
    for num in range(1,10):
        for block in range(len(board)):
            triedRow = [-1]
            foundSpot = False
            for i in range(3):
                row = -1
                while row in triedRow:
                    row = randint(0,2)
                    triedRow.append(row)
                    if " " in board[block][row] and row_availble(block,row,board,num):
                        triedCol = [-1]
                        for j in range(3):
                            col = -1
                            while col in triedCol:
                                col = randint(0,2)
                                triedCol.append(col)
                                if " " == board[block][row][col] and col_available(block,row,col,board,num):
                                    board[block][row][col] = num
                                    foundSpot = True
                                    if foundSpot:
                                        break
                                    if foundSpot:
                                        break
                                    if not foundSpot:
                                        print("Never Fount a Spot for" + str(num) + " in block " + str(block))
                                        return board
def display(borad):
    num=[]
    for i in borad:
        for subI in i :
            for subsubI in subI :
                num.append(subsubI)
    print('----------------------------------------------')
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[0],num[1],num[2],num[9],num[10],num[11],num[18],num[19],num[20]))
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[3],num[4],num[5],num[12],num[13],num[14],num[21],num[22],num[23]))
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[6],num[7],num[8],num[15],num[16],num[17],num[24],num[25],num[26])) 
    print("---------------------------------------") 
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[27],num[28],num[29],num[36],num[37],num[38],num[45],num[46],num[47]))
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[30],num[31],num[32],num[39],num[40],num[41],num[48],num[49],num[50]))
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[33],num[34],num[35],num[42],num[43],num[44],num[51],num[52],num[53])) 
    print("---------------------------------------") 
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[54],num[55],num[56],num[63],num[64],num[65],num[72],num[73],num[74])) 
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[57],num[58],num[59],num[66],num[67],num[68],num[75],num[76],num[77])) 
    print("---------------------------------------") 
    print("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(num[60],num[61],num[62],num[69],num[70],num[71],num[78],num[79],num[80])) 
    print("---------------------------------------") 

borad=build_borad()
borad=fill_borad(borad)
display=display(borad)
build_borad(borad)