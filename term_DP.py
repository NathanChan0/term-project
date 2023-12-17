#Table creatin function
from random import*

def myLCS_DP(seq1 = "", seq2 = "",n = 12):

    #random generates sequences if none inputted
    base_list = ("A","T","C","G")
    if seq1 == "" and seq2 == "":
        for i in range(n):
            nBase1 = choice(base_list)
            nBase2 = choice(base_list)
            seq1 += nBase1
            seq2 += nBase2
            
    # seq2 : vertical,  seq1 :horizontal
    print("Sequence 1:", seq1)
    print("Sequence 2:", seq2)
    
    #### table of zeros with dimension (1+|X|)-by-(1+|Y|)
    opt = []
    for i in range(len(seq2)+1):
        row = []
        for i in range(len(seq1)+1):
            row.append(0)
        opt.append(row)
    # Calculate Optimal score table
    for y in range(1,len(opt)):
        for x in range(1,len(opt[y])):
            #previous x index and y index
            prev_x = opt[y][x-1]
            prev_y = opt[y-1][x]
            #if match add 1, if mismatch previous diagonal index
            if seq1[x-1] == seq2[y-1]:
                diag = opt[y-1][x-1]+1
            else:
                diag = opt[y-1][x-1]
            scores=[prev_x,prev_y,diag]
            #index score is highest between the 3
            opt[y][x] = max(scores)

    if opt[len(opt)-1][len(opt[0])-1] == 0:
        print("No matching subsequences")
        
    
    
    #### Print the final table \
    else:
        for row in range(len(opt)):
            print(f"Row{row}: {opt[row]}")
        TraceBack(seq1,seq2,opt)

def TraceBack(seq1, seq2, table):
    first = ''        # alignment for seq1
    second = ''       # alignment for seq2

    #start reconstruction at bottom-right of table
    # x and y are index of table
    x = len(table[0])-1
    y = len(table)-1
    
    while table[y][x] != 0:
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
            first = seq1[x-1] + first
            second = seq2[y-1] + second
            x -= 1
            y -= 1
            
    #### Print your best alignment
    print("Optimal Alignment:")
    print(first)
    print(second)
    print(f"LCS length: {len(first)}")


dna1 = "AAAGCAGCTGAG"
dna2 = "GACTCTAGTGCA"
table = myLCS_DP(dna1,dna2)
#myLCS_DP()
