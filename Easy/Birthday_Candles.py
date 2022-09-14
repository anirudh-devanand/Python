import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    candles.sort()
    return(candles.count(candles[-1]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

    
print(result)