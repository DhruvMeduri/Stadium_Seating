# BLOCK ALGORITHM IMPLEMENTATION

import math
import numpy as np
import time
# 'block_algo' is the main function in the implementation of the block algorithm. It divides the rectangle into smaller squares corresponing to the max cluster size and then strats filling into the smaller squares sequencially taking care of the edge rectangles in a appropriate manner by filling then with [max(max cluster size,size of the rectangle)] number of seats.
def block_algo(row,col,m):
    global seats
    seats=np.zeros((row,col),dtype='U')
    seats.fill(' ')
    sq=math.ceil(math.sqrt(m))
    flag_a=0
    flag_b=0
    for a in range(sq,col,sq+1):
        flag_a=flag_a+1
        for b in range(0,row):
            seats[b][a]='.'


    for c in range(sq,row,sq+1):
        flag_b=flag_b+1
        for d in range(0,col):
            seats[c][d]='.'

    total=seats.size

    ver=col-(flag_a*(sq+1))
    hor=row-(flag_b*(sq+1))

    ver_edge = ver*sq
    hor_edge = hor*sq

    fam_ver = ver_edge
    fam_hor = hor_edge

    if(m<ver_edge):
        ver_edge=m
        fam_ver=m

    if(m<hor_edge):
        hor_edge=m
        fam_hor=m

    center = m*(flag_a*flag_b)
    e1 = ver_edge*flag_b
    e2 = hor_edge*(flag_a)
    ex = ver*hor
    if m < ex:
        ex = m

    filled= center + e1 + e2 + ex

    per_ratio=(filled/total)*100

    for u in range(0,flag_b):
        for v in range(0,flag_a):

            fill = m
            for i in range(u*(sq+1), (u)*(sq+1)+sq):
                for j in range(v*(sq+1), (v)*(sq+1)+sq):
                    if(fill>0 and seats[i][j]!='X'):

                        seats[i][j]='1'
                        fill=fill-1

    for k in range(0,flag_b):
        ver_fill = fam_ver
        for l in range(k*(sq+1), (k)*(sq+1)+sq):
            for p in range((flag_a)*(sq+1),col):
                if(ver_fill>0):

                    seats[l][p]='1'
                    ver_fill = ver_fill-1


    for q in range(0,flag_a):
        hor_fill = fam_hor
        for r in range((flag_b)*(sq+1),row):
            for s in range(q*(sq+1), (q)*(sq+1)+sq):
                if(hor_fill>0):

                    seats[r][s]='1'
                    hor_fill = hor_fill-1

    edge_fill=ver*hor
    if(edge_fill>m):
        edge_fill=m

    for x in range((flag_b)*(sq+1),row):
        for y in range((flag_a)*(sq+1),col):
            if(edge_fill>0):
                seats[x][y] = '1'
                edge_fill = edge_fill - 1

    return per_ratio

# 'print_format' is used for displaying the final arrangement gien by the 'block_algo' function.
def print_format(l,b,m):
    print('\nPercentage Filled =',block_algo(l,b,m),'%')
    print('\n')
    for r in range(l):
       for c in range(b):
          print(seats[r][c],end = '   ')
       print('\n')

# For plotting:
perf_list = []
time_list = []
for i in range(1,11):
    print(i)
    start= time.time()
    perf = block_algo(21,21,i)
    end = time.time()
    perf_list.append(perf)
    time_list.append(end-start)

print("Performance: ", perf_list)
print("Runtime: ",time_list)
