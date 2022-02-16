import walk_alg
import time
perf_list = []
time_list = []
for i in range(1,26):
    print(i)
    start= time.time()
    obj = walk_alg.walk_on_graph(i,6)
    perf = obj.alg()
    end = time.time()
    perf_list.append(perf)
    time_list.append(end-start)

print("Performance: ", perf_list)
print("Runtime: ",time_list)
