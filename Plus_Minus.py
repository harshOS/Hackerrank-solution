def plusMinus(arr):
    plus,minus,zero = 0,0,0
    for i in range(n):
        if arr[i] > 0:
            plus += 1
        elif arr[i] < 0:
            minus += 1
        else:
            zero += 1
    print(plus/n,'\n',minus/n,'\n',zero/n)
