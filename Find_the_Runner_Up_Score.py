#problem link - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_operation = list(arr)
    max1 = max(arr_operation)
    while(arr_operation.count(max1) != 0):
        arr_operation.remove(max1)
    print(max(arr_operation))

