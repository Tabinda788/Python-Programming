from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__=='__main__':
    t1=time.time()
    # p=Pool(processes=3) TO CREATE ONLY 3 PROCESSES
    p = Pool()
    result = p.map(f,range(100000))
    p.close()
    p.join()
    # result = []

    # for n in array:
    #     result.append(f(n))
    print("Pool took:",time.time()-t1)
    # print(result)
    t2=time.time()
    result = []
    for x in range(100000):
        result.append(f(x))


    print("Serial processing took",time.time()-t2)
