def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[0:4]),sum(arr[1:5]))

miniMaxSum([1, 2, 3, 4, 5])