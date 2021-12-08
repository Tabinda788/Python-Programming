#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# MY SOLTION
lis = []
dic1 = {}
dic2 = {}
def timeConversion(s):
    a = s[0]
    b = s[1]
    c = a.join(b)
    for i in range(0, 2):
        for j in range(1, 13):
            lis.append(j)
            dic1[(j)] = (j)
            m = 13
            while m <= 24:
                for k in range(1, 13):
                    dic2[((k))] = (m)
                    m = m+1
    def merge_values(val1, val2):
        if val1 is None:
            return [val2]
        elif val2 is None:
            return [val1]
        else:
            return [val1, val2]
    dict3 = {
        key: merge_values(dic1.get(key), dic2.get(key))
        for key in set(dic1).union(dic2)
    }
    lis1 = dict3[int(c)]
    if s[8] == "P":
        
        to_append = str(lis1[1])
        sliced = s[2:]
        result = to_append + sliced
        return result
    else:
        to_append = str(lis1[0])
        sliced = s[2:]
        result = to_append + sliced
        return result

if __name__ == '__main__':
   

    s = input()

    result = timeConversion(s)
    print(result)



# Someones solution
def timeConversion(s):
    time = s.split(":")
    print(time)
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    ntime = ':'.join(time)
    return str(ntime[:-2])
    
if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result)
