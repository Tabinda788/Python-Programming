import time
import multiprocessing

# create 2 different processes 1st will calculate square of these numbers and 2nd will calculate cube
square_result = []
def calc_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('square ' + str(n*n))
        square_result.append(n*n)
    print('within a process: result ' + str(square_result))

def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cube ' + str(n*n*n))


if __name__ == "__main__":
    arr = [2,3,8,9]
    p1=multiprocessing.Process(target=calc_square,args=(arr,))
    p2=multiprocessing.Process(target=calc_cube,args=(arr,))
    print('result  '+ str(square_result))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
