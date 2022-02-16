import alg_class
import time
perf_lst = []
time_lst = []
for i in range(1,16):
    print(i)
    start = time.time()
    obj = alg_class.compute_arrangement(i,6)
    configs = obj.printconfig()
    perf = obj.add_final(configs)
    end = time.time()
    perf_lst.append(perf)
    time_lst.append(end-start)
print("Performance:", perf_lst)
print("Runtime: ",time_lst)
