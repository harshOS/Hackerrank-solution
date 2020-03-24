#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    spent = 0
    temp_spent = 0
    count = 0
    for i in range(n):
        for j in range(m):
            if (keyboards[i]+drives[j]) <= b:
                spent = keyboards[i]+drives[j]
                count += 1
            if spent >= temp_spent:
                temp_spent = spent
    if count == 0:
        return -1
    else:
        return temp_spent

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
