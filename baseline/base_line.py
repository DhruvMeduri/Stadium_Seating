# BASELINE ALGORITHM IMPLEMENTATION

import numpy as np              # numpy for 2D arrays
from itertools import product
import math
from os import system

# All the baseline functions follow the basic principle of filling : Leave the alternate rows empty and fill the remaining rows only using a single type of configuration ( length equal to family size and a unit breadth ).

# 'baseline' takes 3 parameters length & breadth of the rectangle and the max cluster size. (returns the percentage of seats filled)
def baseline(row,col,lim):

        global seats
        seats=np.zeros((row,col), dtype='U')
        total=seats.size
        remainder=total

        if(row%2==0):
            for dash in range(1,row,2):
                seats[dash]='-'
                nat=row-1
        else:
            for dash in range(1,row-1,2):
                seats[dash]='-'
                nat=row

        def perf():         # function for calculating ratio of filled seats
            flag=0
            global ratio
            for x, y in product(range(0,row), range(0,col)):
                if(seats[x][y]=='O'):
                    flag=flag+1

            ratio = (flag/total)*100

        for i in range(0,row,2):
            cur=0
            fil=col
            max=lim
            while(cur<=col and max>0):
                if(max<=fil):
                    for k in range(cur,cur+max):
                        seats[i][k]='O'
                    cur=cur+max+1
                    fil=fil-max-1
                else:
                    max=max-1

        perf()
        return ratio

# 'baseline_diamond' takes 2 parameters iagonal size of the diamond and the max cluster size. (returns the percentage of seats filled)
def baseline_diamond(n,lim):

    global set
    set=np.zeros((n,n),dtype='U')
    set.fill(' ')

    # odd1=[3,7,11,15,19,23,27,31,35,39,43,47,51,55,59,63,67,71,75,79,83,87,91,95,99,103]
    # odd2=[5,9,13,17,21,25,29,33,37,41,45,49,53,57,61,65,69,73,77,81,85,89,93,97,101,105]
    # even1=[2,6,10,14,18,22,26,30,34,38,42,46,50,54,58,62,66,70,74,78,82,86,90,94,98,102]
    # even2=[4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104]

    odd1  = [i for i in range(3,n+2,4)]
    odd2  = [i for i in range(5,n+2,4)]
    even1 = [i for i in range(2,n+2,4)]
    even2 = [i for i in range(4,n+2,4)]

    if(n in odd1):
        top=math.ceil(n/2)-1
        for i in range(0,top+1):

            if(i==0):
                set[i][top]='O'

            else:
                for j in range(top-i,top+i+1):

                    set[i][j]='O'

        for p in range(top+1,n):

            if(p==n-1):
                set[p][top]='O'

            else:

                for k in range(p-top,n-(p-top)):

                    set[p][k]='O'

        total_seats=np.count_nonzero(set == 'O')


        for i in range(0,top+1,2):

            if(i==0):
                set[i][top]='X'

            else:
                for j in range(top-i,top+i+1):

                    cur=top-i
                    fil=(top+i+1)-(top-i)
                    max=lim
                    while(cur<=(top+i) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[i][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1

        for p in range(top+1,n,2):
            if(p==n-1):
                set[p][top]='X'

            else:

                for k in range(p-top,n-(p-top)):

                    cur=p-top
                    fil=n-2*p+2*top
                    max=lim
                    while(cur<=(n-(p-top)-1) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[p][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1


        filled_seats=np.count_nonzero(set == 'X')


        per_ratio=(filled_seats/total_seats)*100

        return per_ratio



    elif(n in odd2):
        top=math.ceil(n/2)-1
        for i in range(0,top+1):

            if(i==0):
                set[i][top]='O'

            else:
                for j in range(top-i,top+i+1):

                    set[i][j]='O'

        for p in range(top+1,n):

            if(p==n-1):
                set[p][top]='O'

            else:

                for k in range(p-top,n-(p-top)):

                    set[p][k]='O'

        total_seats=np.count_nonzero(set == 'O')


        for i in range(1,top+1,2):

            if(i==0):
                set[i][top]='X'

            else:
                for j in range(top-i,top+i+1):

                    cur=top-i
                    fil=(top+i+1)-(top-i)
                    max=lim
                    while(cur<=(top+i) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[i][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1

        for p in range(top+1,n,2):

            if(p==n-1):
                set[p][top]='X'

            else:
                for k in range(p-top,n-(p-top)):

                    cur=p-top
                    fil=n-2*p+2*top
                    max=lim
                    while(cur<=(n-(p-top)-1) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[p][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1


        filled_seats=np.count_nonzero(set == 'X')


        per_ratio=(filled_seats/total_seats)*100

        return per_ratio



    elif(n%2==0 and n in even1):
        top=math.ceil(n/2)
        for i in range(0,top):

                for j in range(top-(i+1),top+(i+1)):

                    set[i][j]='O'

        for p in range(top,n-1):

                for k in range(p-top+1,n-(p-top)-1):

                    set[p][k]='O'

        total_seats=np.count_nonzero(set == 'O')


        for i in range(0,top,2):

                for j in range(top-(i+1),top+(i+1)):

                    cur=top-(i+1)
                    fil=(top+(i+1))-(top-(i+1))
                    max=lim
                    while(cur<=(top+i) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[i][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1

        for p in range(top+1,n,2):
                for k in range(p-top+1,n-(p-top)-1):

                    cur=p-top+1
                    fil=n-2*p+2*top-2
                    max=lim
                    while(cur<=(n-(p-top)-2) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[p][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1

        filled_seats=np.count_nonzero(set == 'X')


        per_ratio=(filled_seats/total_seats)*100

        return per_ratio

    elif(n%2==0 and n in even2):
        top=math.ceil(n/2)
        for i in range(0,top):
                for j in range(top-(i+1),top+(i+1)):

                    set[i][j]='O'

        for p in range(top,n-1):
                for k in range(p-top+1,n-(p-top)-1):

                    set[p][k]='O'

        total_seats=np.count_nonzero(set == 'O')


        for i in range(0,top,2):

                for j in range(top-(i+1),top+(i+1)):

                    cur=top-(i+1)
                    fil=(top+(i+1))-(top-(i+1))
                    max=lim
                    while(cur<=(top+i) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[i][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1

        for p in range(top,n,2):
                for k in range(p-top+1,n-(p-top)-1):

                    cur=p-top+1
                    fil=n-2*p+2*top-2
                    max=lim
                    while(cur<=(n-(p-top)-2) and max>0):
                        if(max<=fil):
                            for k in range(cur,cur+max):
                                set[p][k]='X'
                            cur=cur+max+1
                            fil=fil-max-1
                        else:
                            max=max-1

        filled_seats=np.count_nonzero(set == 'X')


        per_ratio=(filled_seats/total_seats)*100

        return per_ratio

# 'baseline_hole' takes 4 parameters side of the square grid, length & breadth of the hole and the max cluster size. (returns the percentage of seats filled)
def baseline_hole(sq_side,h_row,h_col,lim):

        global seats
        seats=np.zeros((sq_side,sq_side), dtype='U')
        seats.fill(' ')
        total=seats.size-(h_row*h_col)

        re=sq_side-h_row
        ce=sq_side-h_col

        for u in range(math.floor(re/2),sq_side-math.ceil(re/2)):
            for v in range(math.floor(ce/2),sq_side-math.ceil(ce/2)):
                seats[u][v]='X'

        for a in range(0,sq_side,2):
            if a in range(math.floor(re/2),sq_side-math.ceil(re/2)):
                cur=0
                fil=math.floor(ce/2)
                max=lim
                while(cur<=math.floor(re/2) and max>0):
                    if(max<=fil):
                        for k in range(cur,cur+max):
                            seats[a][k]='O'
                        cur=cur+max+1
                        fil=fil-max-1
                    else:
                        max=max-1

                cur=sq_side-math.ceil(ce/2)
                fil=math.ceil(ce/2)
                max=lim
                while(cur<=sq_side and max>0):
                    if(max<=fil):
                        for k in range(cur,cur+max):
                            seats[a][k]='O'
                        cur=cur+max+1
                        fil=fil-max-1
                    else:
                        max=max-1

            else:
                cur=0
                fil=sq_side
                max=lim
                while(cur<=sq_side and max>0):
                    if(max<=fil):
                        for k in range(cur,cur+max):
                            seats[a][k]='O'
                        cur=cur+max+1
                        fil=fil-max-1
                    else:
                        max=max-1



        def perf():         #ratio of filled seats
            flag=0
            global ratio
            for x, y in product(range(0,sq_side), range(0,sq_side)):
                if(seats[x][y]=='O'):
                    flag=flag+1

            ratio = (flag/total)*100

        perf()
        return ratio

# 'baseline_print' is used for displaying the final arrangements of different baseline functions corresponding to the argument passed.
def baseline_print():
        row = int(input("Enter number of rows: "))
        col = int(input("Enter number of columns: "))
        lim = int(input("Enter max cluster size: "))
        perc = baseline(row,col,lim)
        print("% filling = ",perc)
        for r in range(row):
            for c in range(col):
               print(seats[r][c],end = '   ')
            print('\n')



# For plotting
perf_lst = []
for i in range(1,11):
    perf_lst.append(baseline(21,21,i))
print(perf_lst)
