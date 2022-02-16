from max_cluster_rectangle import config_shape
def allsets(size,configs):
      # Input: All allowed configurations and dimension of stadium/theatre.
      # Output: Returns all the sets.
      tconfig=[]         
      for k in configs:
        config = []   
        for i in range(k[1]*k[2]):
            if i not in k[0]:
                config.append(i)                
        for r in range(size - k[1] + 1):            
            for c in range(size - k[2] + 1):
              se = set()
              neigh = set()
              for i in config :
                  a = r + int(i/k[2])
                  b = c + (i % k[2])
                  se.add((size * a) + b)
              for i in k[0]:
                  a = r + int(i/k[2])
                  b = c + (i % k[2])
                  neigh.add((size * a) + b)
              for i in range(k[1]):
                  if c!=0:
                      num = (r+i)*(size) + c - 1
                      if (num+1) in se:
                          neigh.add(num)                                     
                  if c!=(size-k[2]):
                      num = (r+i)*(size) + c + k[2]
                      if (num-1) in se:
                          neigh.add(num)                            
              for i in range(k[2]):
                  if r!=0:
                      num = (r-1)*(size) + c + i
                      if (num + size) in se:
                          neigh.add(num)
                  if r != size - k[1]:
                      num = (r + k[1])*(size) + c + i
                      if( num - size) in se:
                          neigh.add(num)
              tconfig.append([se,neigh])    
      return tconfig

