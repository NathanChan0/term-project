from random import*

def myLCS_Re(seq1 = " ",seq2 =" ", n = 12):

    #random generates sequences if none inputted
    base_list = ("A","T","C","G")
    if seq1 == " " and seq2 == " ":
        for i in range(n):
            nBase1 = choice(base_list)
            nBase2 = choice(base_list)
            seq1 += nBase1
            seq2 += nBase2
        seq1 = seq1[1:]
        seq2 = seq2[1:]

    #generates alignment table
    table = []
    for i in range(len(seq2)+1):
        row = []
        for i in range(len(seq1)+1):
            row.append(0)
        table.append(row)
    # Calculate Optimal score table
    for y in range(1,len(table)):
        for x in range(1,len(table[y])):
            #previous x index and y index
            prev_x = table[y][x-1]
            prev_y = table[y-1][x]
            #if match add 1, if mismatch previous diagonal index
            if seq1[x-1] == seq2[y-1]:
                diag = table[y-1][x-1]+1
            else:
                diag = table[y-1][x-1]
            scores=[prev_x,prev_y,diag]
            #index score is highest between the 3
            table[y][x] = max(scores)

    x = len(table[0])-1
    y = len(table)-1
    
    check = False
    if table[y][x] == 0:
        return ""
    
    else:
        while check == False:
            if table[y][x] == table[y][x-1] and table[y][x] == table[y-1][x] and table[y][x] == table[y-1][x-1]:
                x -= 1
                y -= 1
            elif table[y][x] == table[y][x-1] and table[y][x] == table[y-1][x] and table[y][x] == table[y-1][x-1]+1:
                x -= 1
                
            elif table[y][x] == (table[y][x-1] + 1) and table[y][x] == table[y-1][x]:
                y -= 1
                    
            elif table[y][x] == table[y][x-1] and table[y][x] == (table[y-1][x] + 1):
                x -= 1
                    
            elif table[y][x] == (table[y][x-1] + 1) and table[y][x] == (table[y-1][x] + 1):
                first = seq1[x-1]
                second = seq2[y-1]
                x -= 1
                y -= 1
                check = True
                return myLCS_Re(seq1[:x],seq2[:y]) + first


def main():
    print(len(myLCS_Re(n=20)))

main()


        
