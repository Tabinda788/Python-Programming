import concurrent.futures
import time
square_result = []
cube_result = []
def calc_square(numbers):
    for n in numbers:
        time.sleep(2)
        square_result.append(n*n)

def calc_cube(numbers):
    for n in numbers:
        time.sleep(2)
        cube_result.append(n*n*n)


arr = [2,3,8,9]


start = time.time()
calc_square(arr)
calc_cube(arr)
end = time.time()
print("Time taken without executor", end-start)


start = time.time()
with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(calc_square,arr)
    squre = future.result()
    future = executor.submit(calc_cube,arr)
    cube = future.result()
end = time.time()
print("Timer taken with executor ", end-start)
