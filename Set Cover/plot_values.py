import alg_class
import time
perf_lst = []
time_lst = []
for i in range(1,9):
    print(i)
    start = time.time()
    obj = alg_class.compute_arrangement(21,i)
    configs = obj.printconfig()
    perf = obj.add_final(configs)
    end = time.time()
    perf_lst.append(perf)
    time_lst.append(end-start)
print("Performance:", perf_lst)
print("Runtime: ",time_lst)
