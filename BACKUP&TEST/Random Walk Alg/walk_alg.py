import numpy as np
import math
import random
import time
class walk_on_graph:
    def __init__(self,side,m):
        self.side = side
        n2 = side*side
        self.m = m
        self.marker = np.zeros(n2)
        self.ver_lst = list(range(0, n2))# this is to store the remaining vertices in the graph
        for i in range(n2):
            if i>=312:
               self.ver_lst.remove(i)
               self.marker[i] = 3
        for r in range((math.floor(12/2) - math.floor(5/2)),math.floor(12/2) - math.floor(5/2) + 5 ):
           for c in range((math.floor(26/2) - math.floor(5/2)),math.floor(26/2) - math.floor(5/2) + 5 ):
                self.ver_lst.remove(r*self.side + c)
                self.marker[r*self.side + c] = 3
        self.total = self.count_zeros()
    def remove_vertex(self,x):
        self.ver_lst.remove(x)


    def rand_walk(self, start):
        walk_memory = [start]
        #print("1")
        for i in range(self.m - 1):
           #print("2")
           bound = 1
           c =1
           # This is the code to make one step
           while(c!=0 and bound <= 5000):
              #print("3")
              step = random.randint(1,4)
              if step == 1 and start % self.side!=0 and (start - 1) in self.ver_lst:
                  walk_memory.append(start-1)
                  start = start - 1
                  c = 0
              elif step == 2 and math.ceil(start/self.side)!=0 and (start - self.side) in self.ver_lst:
                  walk_memory.append(start-self.side)
                  start = start-self.side
                  c = 0
              elif step == 3 and start % self.side!=(self.side)-1 and (start + 1) in self.ver_lst:
                  walk_memory.append(start+1)
                  start = start+1
                  c = 0
              elif step == 4 and math.ceil(start/self.side)!=self.side - 1 and (start + self.side) in self.ver_lst:
                  walk_memory.append(start + self.side)
                  start = start + self.side
                  c = 0
              bound = bound + 1
        walk_memory = list(set(walk_memory))
        #print(walk_memory)
        return walk_memory

    def check_polygon_adjacent(self,poly):
        adj = []
        for i in poly:
            if (i+1) in self.ver_lst and (i+1) not in poly and (i+1) not in adj and i%self.side != self.side - 1:
                adj.append(i+1)

            if (i-1) in self.ver_lst and (i-1) not in poly and (i-1) not in adj and i%self.side != 0:
                adj.append(i-1)

            if (i-self.side) in self.ver_lst and (i-self.side) not in poly and (i-self.side) not in adj and i/self.side != 0:
                adj.append(i-self.side)

            if (i+self.side) in self.ver_lst and (i+self.side) not in poly and (i+self.side) not in adj and i/self.side != self.side-1:
                adj.append(i+self.side)

        return adj

    def update(self, adj, poly):
        for i in poly:
            #print("3")
            self.marker[i] = 1
            self.remove_vertex(i)
        for j in adj:
            #print("4")
            self.marker[j] = 2
            self.remove_vertex(j)
        #return self.marker

    def count_zeros(self):
        count = 0
        for i in self.marker:
            if i==0:
                count = count + 1
        return count

    def alg(self):
        while(self.count_zeros()!=0):
            #print("1")
            start = random.choice(self.ver_lst)
            #print("Start: ",start)
            poly = self.rand_walk(start)
            adj = self.check_polygon_adjacent(poly)
            #for i in range(self.n2):
                #self.marker[i] = self.update(adj,poly)[i]
            #self.marker = self.update(adj,poly)
            self.update(adj,poly)
            #self.out_seating()
        # This is to compute the performance
        count = 0
        for i in self.marker:
            if i == 1:
                count = count + 1
        return((100*count)/(self.total))


    def out_seating(self):
        for i in range(self.side):
            for j in range(self.side):
                k = int((i*self.side) + j)
                if self.marker[k]==1:
                   print(int(self.marker[k]), end = '     ')
                else:
                   print(' ', end='     ')
            print("\n")

#start = time.time()
obj = walk_on_graph(26,6)
perf = obj.alg()
print("Occupance: ", perf)
print("Total:", obj.total)
#end = time.time()
#print("Runtime: ",end-start)
obj.out_seating()
