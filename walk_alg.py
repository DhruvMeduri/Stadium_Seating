import numpy as np
import math
import random
class walk_on_graph:
    side = 4
    n2 = side*side
    graph = np.zeros([n2,n2])
    m = 4
    marker = np.zeros(n2)
    ver_lst = list(range(0, n2))# this is to store the remaining vertices in the graph
    '''
    def make_graph(self):
        n = self.n2
        s = self.side
        for i in range(n):
            if i%s == 0 and math.floor(i/s)!=0 and math.floor(i/s)!=s-1:#not first or last row but first column
               #print("1")
               self.graph[i][i+1] = 1
               self.graph[i][i+s] = 1
               self.graph[i][i-s] = 1
            elif i%s == 0 and math.floor(i/s)==0:#first row and first column
               #print("2")
               self.graph[i][i+1] = 1
               self.graph[i][i+s] = 1
            elif i%s == 0 and math.floor(i/s)==s-1:#first column and last row
               #print("3")
               self.graph[i][i+1] = 1
               self.graph[i][i-s] = 1
            elif i%s == s-1 and math.floor(i/s)!=0 and math.floor(i/s)!=s-1:#not first or last row but last column
               #print("4")
               self.graph[i][i-1] = 1
               self.graph[i][i+s] = 1
               self.graph[i][i-s] = 1
            elif i%s == s-1 and math.floor(i/s)==0:#first row and last column
               #print("5")
               self.graph[i][i-1] = 1
               self.graph[i][i+s] = 1
            elif i%s == s-1 and math.floor(i/s)==s-1:#last row and last column
               #print("6")
               self.graph[i][i-1] = 1
               self.graph[i][i-s] = 1
            elif math.floor(i/s) == 0 and i%s!=0 and i%s!=s-1:#first row but not first or last column
               #print("7")
               self.graph[i][i-1] = 1
               self.graph[i][i+1] = 1
               self.graph[i][i+s] = 1
            elif math.floor(i/s) == s-1 and i%s!=0 and i%s!=s-1:#last row but not first or last column
               #print("8")
               self.graph[i][i-1] = 1
               self.graph[i][i+1] = 1
               self.graph[i][i-s] = 1
            else:
               #print("9")
               self.graph[i][i-1] = 1
               self.graph[i][i+1] = 1
               self.graph[i][i-s] = 1
               self.graph[i][i+s] = 1
    '''
    def remove_vertex(self,x):
        self.ver_lst.remove(x)
        #removing the vertex
        #self.graph = np.delete(self.graph,x,0)
        #self.graph = np.delete(self.graph,x,1)

    def rand_walk(self, start):
        walk_memory = [start]
        #print("1")
        for i in range(self.m):
           #print("2")
           bound = 1
           c =1
           while(c!=0 and bound <= 4*(self.m)):
              #print("3")
              step = random.randint(1,4)
              if step == 1 and start % self.side!=0 and (start - 1) in self.ver_lst:
                  walk_memory.append(start-1)
                  c = 0
              elif step == 2 and math.ceil(start/self.side)!=0 and (start - self.side) in self.ver_lst:
                  walk_memory.append(start-self.side)
                  c = 0
              elif step == 3 and start % self.side!=(self.side)-1 and (start +1) in self.ver_lst:
                  walk_memory.append(start+1)
                  c = 0
              elif step == 4 and math.ceil(start/self.side)!=self.side-  1 and (start + self.side) in self.ver_lst:
                  walk_memory.append(start + self.side)
                  c = 0
              bound = bound + 1
        return walk_memory

    def check_polygon_adjacent(self,poly):
        adj = []
        print("2")
        for i in poly:
            if (i+1) in self.ver_lst and (i+1) not in poly and (i+1) not in adj:
                adj.append(i+1)

            elif (i-1) in self.ver_lst and (i-1) not in poly and (i-1) not in adj:
                adj.append(i+1)

            elif (i-self.side) in self.ver_lst and (i-self.side) not in poly and (i-self.side) not in adj:
                adj.append(i-self.side)

            elif (i+self.side) in self.ver_lst and (i+self.side) not in poly and (i+self.side) not in adj:
                adj.append(i+self.side)

        return adj

    def update(self, adj, poly):
        print("3")
        for i in poly:
            self.marker[i] = 1
            self.remove_vertex(i)
        for j in adj:
            self.marker[j] = 2
            self.remove_vertex(j)
        return marker

    def count_zeros(self):
        count = 0
        for i in self.marker:
            if i==0:
                count = count + 1
        return count
    def alg(self):
        while(self.count_zeros()!=0):
            start = random.choice(self.ver_lst)
            poly = self.rand_walk(start)
            adj = self.check_polygon_adjacent(poly)
            for i in range(self.n2):
                self.marker[i] = self.update(adj,poly)[i]
    def out_seating(self):
        for i in range(self.side):
            for j in range(self.side):
                print(self.marker[(i*side) + j] + " ")
            print("\n")

obj = walk_on_graph()
obj.alg()
obj.out_seating()
#obj.make_graph()
#print(obj.graph)
#obj.remove_vertex(15)
#print(obj.graph)
