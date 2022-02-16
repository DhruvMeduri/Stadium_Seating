import numpy as np
import math
import matplotlib.pyplot as plt
from itertools import combinations
from os import system
from collections import defaultdict
def dupli(test_list):
    res = []
    for i in test_list:
      if i not in res:
         res.append(i)
    return res

def seq(msize):
  # Input: Max family size
  # Output: List of all allowed spanning rectangles.
  shapes = []
  for csize in range(1,msize + 1):
    for l in range(1,csize+1):
        for b in range(1,csize+1):
            if (l + b <= csize + 1)  and (l * b >= csize):
                wastage = (l*b) - csize
                shapes.append([l,b,wastage])

  return shapes


def check_config_2(ar,l,b):
    # Input: A cofiguration
    # Output: Checks if every row and column is occupied.
    for r in range(l):
        flag = 0
        for c in range(b):
            if ar[r][c] == 1:
                flag = 1
        if flag == 0:
            return 0
    for c in range(b):
        flag = 0
        for r in range(l):
            if ar[r][c] == 1:
                flag = 1
        if flag == 0:
            return 0
    return 1

def graph_check(ar,l,b):
    # Input: A configuration
    # Output: Checks if the configuration is continuous.
    index_list=[]
    pair_list=[]


    for s in range(0,l*b):
        index_list.append(s)
        #print(index_list[s])
        if ar[math.floor(s/b)][s%b]==1:
            pair_list.append(s)


    # This class represents a directed graph using adjacency list representation
    class Graph:

        def __init__(self, vertices):
            # No. of vertices
            self.V = vertices
            self.lst = []
            # default dictionary to store graph
            self.graph = defaultdict(list)


        # function to add an edge to graph
        def addEdge(self, u, v):
            self.graph[u].append(v)

        '''A recursive function to print all paths from 'u' to 'd'.
        visited[] keeps track of vertices in current path.
        path[] stores actual vertices and path_index is current
        index in path[]'''

        def printAllPathsUtil(self, u, d, visited, path):

            # Mark the current node as visited and store in path
            visited[u]= True
            path.append(u)

            # If current vertex is same as destination, then print
            # current path[]
            if u == d:
                k = []
                for i in path:
                    k.append(i)

                self.lst.append(k)
                #print(path)

            else:
                # If current vertex is not destination
                # Recur for all the vertices adjacent to this vertex
                for i in self.graph[u]:
                    if visited[i]== False:
                        self.printAllPathsUtil(i, d, visited, path)

            # Remove current vertex from path[] and mark it as unvisited
            path.pop()
            visited[u]= False


        # Prints all paths from 's' to 'd'
        def printAllPaths(self, s, d):

            # Mark all the vertices as not visited
            visited =[False]*(self.V)

            # Create an array to store paths
            path = []

            # Call the recursive helper function to print all paths
            self.printAllPathsUtil(s, d, visited, path)

    #Create a graph given in the above diagram

    g = Graph(l*b)
    #print('l,b',l,b)
    for i in range(0,l):
        for j in range(0,b):
            #print('cur coord',i,j)
            if i!=(l-1) and j!=(b-1) and i!=0 and j!=0:
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-1])

                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+b])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-b])

                # print('a',index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                # print('a',index_list[((i*b)+j)], index_list[((i*b)+j)-1])

                # print('a',index_list[((i*b)+j)], index_list[((i*b)+j)+b])
                # print('a',index_list[((i*b)+j)], index_list[((i*b)+j)-b])

            if i==0 and j==0:
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+b])

                # print('b',index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                # print('b',index_list[((i*b)+j)], index_list[((i*b)+j)+b])
            if i==0 and j==(b-1):
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+b])

                # print('c',index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                # print('c',index_list[((i*b)+j)], index_list[((i*b)+j)+b])
            if i==(l-1) and j==0:
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-b])

                # print('d',index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                # print('d',index_list[((i*b)+j)], index_list[((i*b)+j)-b])
            if i==(l-1) and j==(b-1):
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-b])
                # print('e',index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                # print('e',index_list[((i*b)+j)], index_list[((i*b)+j)-b])


            if i==0 and j!=0 and j!=(b-1):
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+b])
                # print('f',index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                # print('f',index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                # print('f',index_list[((i*b)+j)], index_list[((i*b)+j)+b])
            if i==(l-1) and j!=0 and j!=(b-1):
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-b])
                # print('g',index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                # print('g',index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                # print('g',index_list[((i*b)+j)], index_list[((i*b)+j)-b])
            if j==0 and i!=0 and i!=(l-1):
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-b])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+b])
                # print('h',index_list[((i*b)+j)], index_list[((i*b)+j)+1])
                # print('h',index_list[((i*b)+j)], index_list[((i*b)+j)-b])
                # print('h',index_list[((i*b)+j)], index_list[((i*b)+j)+b])
            if j==(b-1) and i!=0 and i!=(l-1):
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)-b])
                g.addEdge(index_list[((i*b)+j)], index_list[((i*b)+j)+b])
                # print('i',index_list[((i*b)+j)], index_list[((i*b)+j)-1])
                # print('i',index_list[((i*b)+j)], index_list[((i*b)+j)-b])
                # print('i',index_list[((i*b)+j)], index_list[((i*b)+j)+b])

    #print(g.graph)
    #print ("Following are all different paths from % d to % d :" %(s, d))
    # y=pair_list[0]
    # pair_list.pop(0)
    #print('----------------')
    #print('s',pair_list)
    for p in range(1,len(pair_list)):
            #print(pair_list[0],pair_list[p])
            g.lst=[]
            g.printAllPaths(pair_list[0],pair_list[p])
            #print('lst',g.lst)
            for a in g.lst:
                flag=0
                #print(a)
                for b in a:
                    #print(b)
                    if(b not in pair_list):
                        flag=1
                        break
                if(flag==0):
                    break

            if flag==1:
                return 0
    return 1
    #print(g.lst)

def printconfig(shapes):
    # Input: List of spanning rectangles.
    # Output: List of allowed configurations.
    total=0
    con=[]
    for i in shapes:
        #print(i)
        a = i[0]*i[1]
        ar = [[ 1 for x in range(i[1])] for y in range(i[0])]
        if(i[2]==0):
            total=total+1
            #printformat0(ar,i[0],i[1])
            con.append([[],i[0],i[1]])
            #print([i[0],i[1],i[2],[]])
            #ele = input("Press any key")
        if( i[2] != 0):
          lst = [0 for k in range(a)]
          for k in range(a):
            lst[k]=k
          comb = combinations (lst,i[2])
          for j in comb:
              j=list(j)
              j.sort()
              ar = [[ 1 for x in range(i[1])] for y in range(i[0])]
              for k in range(i[2]):
                c = j[k]
                d=int(c/i[1])
                ar[d][c%i[1]]=0
              if graph_check(ar,i[0],i[1]) and check_config_2(ar,i[0],i[1]) :
                 total=total+1
                 #printformat0(ar,i[0],i[1])
                 #print([i[0],i[1],i[2],j])
                 con.append([j,i[0],i[1]])
                 #ele = input("Press any key")
    #print(total)
    #print(con)
    return con

def plot_config():
    # Input: Max family size
    # Output: Number of configs vs family size graph
    max_size = int(input("Enter the maximum config size: "))
    shapes = seq(max_size)
    x_list = [(i+1) for i in range(max_size)]
    y_list = [0 for i in range(max_size)]
    for i in shapes:
        #print(i)
        a = i[0]*i[1]
        ar = [[ 1 for x in range(i[1])] for y in range(i[0])]
        if(i[2]==0):
            num = i[0]*i[1] - i[2]
            y_list[num - 1] = y_list[num - 1] + 1
        if( i[2] != 0):
          lst = [0 for k in range(a)]
          for k in range(a):
            lst[k]=k
          comb = combinations (lst,i[2])
          for j in comb:
              j=list(j)
              j.sort()
              ar = [[ 1 for x in range(i[1])] for y in range(i[0])]
              for k in range(i[2]):
                c = j[k]
                d=int(c/i[1])
                ar[d][c%i[1]]=0
              if graph_check(ar,i[0],i[1]) and check_config_2(ar,i[0],i[1]) :
                 num = i[0]*i[1] - i[2]
                 y_list[num - 1] = y_list[num - 1] + 1


    plt.title("Number of Configs vs Cluster Size")
    plt.xlabel("Cluster size")
    plt.ylabel("Number of configurations")
    plt.plot(x_list,y_list,marker='X')
    print(y_list)
    #plt.axis([0,15,0,100])
    plt.show()

def show_configs_of_size(msize):
     # Input: Max family Size
     # Output: Prints all allowed configurations.
     total = 0
     con = []
     shapes = seq(msize)
     for i in shapes:
        #print(i)
        a = i[0]*i[1]
        ar = [[ 1 for x in range(i[1])] for y in range(i[0])]
        if(i[2]==0):
            total=total+1
            #printformat0(ar,i[0],i[1])
            con.append([[],i[0],i[1]])
            for r in range(i[0]):
                for c in range(i[1]):
                    if ((r*i[1]) + c) in []:

                          print(" ",end='   ')
                    else:
                          print('1',end='   ')
                print("\n")
            print([[],i[0],i[1]])
            char = input("Press enter for next configuration: ")
            system("cls")
            #print([i[0],i[1],i[2],[]])
            #ele = input("Press any key")
        if( i[2] != 0):
          lst = [0 for k in range(a)]
          for k in range(a):
            lst[k]=k
          comb = combinations (lst,i[2])
          for j in comb:
              j=list(j)
              j.sort()
              ar = [[ 1 for x in range(i[1])] for y in range(i[0])]
              for k in range(i[2]):
                c = j[k]
                d=int(c/i[1])
                ar[d][c%i[1]]=0
              if graph_check(ar,i[0],i[1]) and check_config_2(ar,i[0],i[1]) :
                 total=total+1
                 #printformat0(ar,i[0],i[1])
                 #print([i[0],i[1],i[2],j])
                 con.append([j,i[0],i[1]])
                 for r in range(i[0]):
                    for c in range(i[1]):
                       print(ar[r][c],end = "   ")
                    print("\n")
                 print([j,i[0],i[1]])
                 char = input("Press enter for next configuration: ")
                 system("cls")
                 #ele = input("Press any key")
    #print(total)
    #print(con)
     print("Total number of configurations: "+ str(total))
