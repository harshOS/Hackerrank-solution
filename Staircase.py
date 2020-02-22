def staircase(n):
    for i in range(1,n+1):
        string = (n-i)*' ' + (i*'#')
        print(string)

staircase(6)