#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=[]
    neg=[]
    zer=[]
    for i in arr :
        if i > 0 :
            pos.append(i) 
        elif i < 0 :
            neg.append(i)
        else :
            zer.append(i)  
    pos_por = (len(pos))/len(arr)
    neg_por = (len(neg))/len(arr)
    zer_por = (len(zer))/len(arr)
    print(pos_por)
    print(neg_por)
    print(zer_por)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
