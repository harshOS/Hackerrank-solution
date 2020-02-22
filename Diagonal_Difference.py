def diagonalDifference(n,arr):
    sum1 = 0
    sum2 = 0
    # Write your code here
    for i in range(n):
        sum1 += arr[i][i]
        sum2 += arr[i][(n-1)-i]
    return abs(sum1 - sum2)
    print(sum1-sum2)

print(diagonalDifference(3,[[11, 2, 4],[4, 5, 6],[10, 8, -12 ]]))