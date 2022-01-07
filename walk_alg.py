import numpy as np
import math
import random
class walk_on_graph:
    side = 10
    n2 = side*side
    graph = np.zeros([n2,n2])
    m = 4
    marker = np.zeros(n2)
    ver_lst = list(range(0, n2))# this is to store the remaining vertices in the graph

    def remove_vertex(self,x):
        self.ver_lst.remove(x)
        #removing the vertex
        #self.graph = np.delete(self.graph,x,0)
        #self.graph = np.delete(self.graph,x,1)

    def rand_walk(self, start):
        walk_memory = [start]
        #print("1")
        for i in range(self.m - 1):
           #print("2")
           bound = 1
           c =1
           while(c!=0 and bound <= 4000*(self.m)):
              #print("3")
              step = random.randint(1,4)
              if step == 1 and start % self.side!=0 and (start - 1) in self.ver_lst and (start-1):
                  walk_memory.append(start-1)
                  c = 0
              elif step == 2 and math.ceil(start/self.side)!=0 and (start - self.side) in self.ver_lst and (start-self.side):
                  walk_memory.append(start-self.side)
                  c = 0
              elif step == 3 and start % self.side!=(self.side)-1 and (start + 1) in self.ver_lst and (start+1):
                  walk_memory.append(start+1)
                  c = 0
              elif step == 4 and math.ceil(start/self.side)!=self.side - 1 and (start + self.side) in self.ver_lst and (start+self.side):
                  walk_memory.append(start + self.side)
                  c = 0
              bound = bound + 1

        walk_memory = list(set(walk_memory))
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
        print("Remaining: ",self.ver_lst)
        print("Family: ",poly)
        print("Wastage: ",adj)
        for i in poly:
            #print("3")
            self.marker[i] = 1
            self.remove_vertex(i)
        for j in adj:
            #print("4")
            self.marker[j] = 2
            self.remove_vertex(j)
        return self.marker

    def count_zeros(self):
        count = 0
        for i in self.marker:
            if i==0:
                count = count + 1
        return count
    def alg(self):
        while(self.count_zeros()!=0):
            print("1")
            start = random.choice(self.ver_lst)
            print("Start: ",start)
            poly = self.rand_walk(start)
            adj = self.check_polygon_adjacent(poly)
            #for i in range(self.n2):
                #self.marker[i] = self.update(adj,poly)[i]
            self.marker = self.update(adj,poly)
            self.out_seating()
    def out_seating(self):
        for i in range(self.side):
            for j in range(self.side):
                k = int((i*self.side) + j)
                print(int(self.marker[k]), end = '       ')
            print("\n")

obj = walk_on_graph()

obj.alg()
#obj.out_seating()
#obj.make_graph()
#print(obj.graph)
#obj.remove_vertex(15)
#print(obj.graph)
# for plotting
